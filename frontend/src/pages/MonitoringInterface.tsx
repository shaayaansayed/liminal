import React, { useEffect, useState, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowLeftIcon, RefreshCwIcon } from 'lucide-react'
import TranscriptionPanel from '../components/TranscriptionPanel'
import AlertsPanel from '../components/AlertsPanel'
import { API_BASE_URL } from '../config/api'

interface MonitoringInterfaceProps {
  zoomUrl: string
  sessionType?: 'real' | 'zoom-simulation' | 'text-simulation' | 'demo-simulation'
}

interface Alert {
  id: string
  type: string
  message: string
  timestamp: string
  participant?: string
  participant_id?: string
  silent_duration?: number
}

interface TranscriptWord {
  text: string
  start_timestamp: number
  end_timestamp: number | null
}

interface TranscriptSegment {
  participant_id: string
  participant_name: string
  is_partial: boolean
  words: TranscriptWord[]
  timestamp: string
}

interface TranscriptionEntry {
  id: number
  speaker: string
  text: string
  timestamp: string
  isPartial?: boolean
}

const MonitoringInterface: React.FC<MonitoringInterfaceProps> = ({ zoomUrl, sessionType = 'real' }) => {
  const navigate = useNavigate()
  const [transcription, setTranscription] = useState<TranscriptionEntry[]>([])
  const [alerts, setAlerts] = useState<Alert[]>([])
  const [wsStatus, setWsStatus] = useState<string>("Disconnected")
  const [isLoadingTranscript, setIsLoadingTranscript] = useState(false)
  const ws = useRef<WebSocket | null>(null)
  const transcriptIdCounter = useRef(0)

  // Fetch existing transcript on mount
  useEffect(() => {
    fetchTranscript()
  }, [])

  // Fetch transcript from API
  const fetchTranscript = async () => {
    setIsLoadingTranscript(true)
    try {
      const response = await fetch(`${API_BASE_URL}/api/transcript?format=json`)
      if (response.ok) {
        const data = await response.json()
        const entries = convertSegmentsToEntries(data.transcript)
        setTranscription(entries)
      }
    } catch (error) {
      console.error('Error fetching transcript:', error)
    } finally {
      setIsLoadingTranscript(false)
    }
  }

  // Convert transcript segments to transcription entries
  const convertSegmentsToEntries = (segments: TranscriptSegment[]): TranscriptionEntry[] => {
    return segments.map(segment => {
      const text = segment.words.map(w => w.text).join(' ')
      const timestamp = segment.words[0]?.start_timestamp 
        ? new Date(Date.now() - (Date.now() - segment.words[0].start_timestamp * 1000)).toISOString()
        : segment.timestamp
      
      return {
        id: transcriptIdCounter.current++,
        speaker: segment.participant_name,
        text: text,
        timestamp: timestamp,
        isPartial: segment.is_partial
      }
    })
  }

  // WebSocket connection management
  useEffect(() => {
    const connectWebSocket = () => {
      // Get the base URL and construct WebSocket URL
      const baseUrl = API_BASE_URL;
      
      // Handle both development and production environments
      let wsUrl: string;
      
      if (baseUrl.startsWith('https://')) {
        // Production: Use wss:// for secure WebSocket
        wsUrl = baseUrl.replace('https://', 'wss://') + '/ws/alerts';
      } else if (baseUrl.startsWith('http://')) {
        // Development: Use ws:// for non-secure WebSocket
        wsUrl = baseUrl.replace('http://', 'ws://') + '/ws/alerts';
      } else {
        // Fallback
        wsUrl = 'ws://localhost:8000/ws/alerts';
      }
      
      console.log('Connecting to WebSocket:', wsUrl);
      
      ws.current = new WebSocket(wsUrl);

      ws.current.onopen = () => {
        console.log('WebSocket connected');
        setWsStatus("Connected");
      };

      ws.current.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          console.log('WebSocket message received:', message);

          if (message.type === 'silence_alert') {
            const newAlert: Alert = {
              id: `${message.participant_id}-${Date.now()}`,
              type: 'silence',
              message: `${message.participant} has not spoken for ${message.silent_duration} seconds`,
              timestamp: message.timestamp,
              participant: message.participant,
              participant_id: message.participant_id,
              silent_duration: message.silent_duration
            };
            
            setAlerts(prev => [...prev, newAlert]);
            console.log('Silence alert added:', newAlert);
          } else if (message.type === 'transcript_update') {
            // Handle real-time transcript updates
            const newTranscription: TranscriptionEntry = {
              id: transcriptIdCounter.current++,
              speaker: message.participant || 'Unknown',
              text: message.text || '',
              timestamp: new Date().toISOString(),
              isPartial: message.event === 'partial'
            };
            
            if (message.event === 'partial') {
              // For partial updates, replace the last partial entry from the same speaker
              setTranscription(prev => {
                const lastIndex = prev.findLastIndex(
                  entry => entry.speaker === newTranscription.speaker && entry.isPartial
                );
                
                if (lastIndex >= 0) {
                  const updated = [...prev];
                  updated[lastIndex] = newTranscription;
                  return updated;
                }
                
                return [...prev, newTranscription];
              });
            } else {
              // For final updates, remove any partial entries from the same speaker and add the final
              setTranscription(prev => {
                const filtered = prev.filter(
                  entry => !(entry.speaker === newTranscription.speaker && entry.isPartial)
                );
                return [...filtered, newTranscription];
              });
            }
            
            console.log('Transcription added:', newTranscription);
          } else if (message.type === 'participant_event') {
            // Handle participant events
            const alertMessage = message.event === 'join' 
              ? `${message.participant} joined the meeting`
              : `${message.participant} left the meeting`;
              
            const newAlert: Alert = {
              id: `participant-${Date.now()}`,
              type: 'info',
              message: alertMessage,
              timestamp: new Date().toISOString()
            };
            
            setAlerts(prev => [...prev, newAlert]);
          } else if (message.type === 'indicator_triggered') {
            // Handle custom indicator alerts from the backend
            const data = message.data;
            const newAlert: Alert = {
              id: `${data.id}-${data.timestamp}`,
              type: data.id, // e.g., 'pace_too_fast'
              message: `${data.name}: ${data.justification}`,
              // Convert Unix timestamp (seconds) to ISO string
              timestamp: new Date(data.timestamp * 1000).toISOString(),
            };
            
            setAlerts(prev => [...prev, newAlert]);
            console.log('Indicator alert added:', newAlert);
          } else if (message.type === 'clear_alerts') {
            // Clear all alerts when session is reset
            setAlerts([]);
            setTranscription([]);
          } else if (message.type === 'transcript_cleared') {
            // Clear transcript when session is reset
            setTranscription([]);
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      ws.current.onclose = () => {
        console.log('WebSocket disconnected');
        setWsStatus("Disconnected");
        
        // Reconnect after 3 seconds
        setTimeout(() => {
          console.log('Attempting to reconnect...');
          connectWebSocket();
        }, 3000);
      };

      ws.current.onerror = (error) => {
        console.error('WebSocket error:', error);
        setWsStatus("Error");
      };
    };

    connectWebSocket();

    // Cleanup on component unmount
    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, []);

  const handleBack = async () => {
    // Fire-and-forget reset session call
    fetch(`${API_BASE_URL}/api/reset-session`, { method: 'POST' }).catch(() => {})
    navigate('/')
  }

  const handleRefreshTranscript = () => {
    fetchTranscript()
  }

  return (
    <div className="flex flex-col w-full h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-6 py-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center">
            <button
              onClick={handleBack}
              className="flex items-center text-gray-600 hover:text-gray-900"
            >
              <ArrowLeftIcon className="h-4 w-4 mr-1" />
              <span>Back</span>
            </button>
            <h1 className="ml-6 text-xl font-semibold text-gray-800">
              Session Monitoring
            </h1>
          </div>
          <div className="flex items-center space-x-4">
            <button
              onClick={handleRefreshTranscript}
              disabled={isLoadingTranscript}
              className="flex items-center px-3 py-1 text-sm text-gray-600 hover:text-gray-900 disabled:opacity-50"
              title="Refresh transcript"
            >
              <RefreshCwIcon className={`h-4 w-4 mr-1 ${isLoadingTranscript ? 'animate-spin' : ''}`} />
              Refresh
            </button>
            <div className={`px-3 py-1 rounded-full text-sm ${
              wsStatus === 'Connected' 
                ? 'bg-green-100 text-green-800' 
                : wsStatus === 'Error' 
                ? 'bg-red-100 text-red-800' 
                : 'bg-gray-100 text-gray-800'
            }`}>
              WebSocket: {wsStatus}
            </div>
            <div className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
              {sessionType === 'text-simulation' ? 'Text Simulation' : 
               sessionType === 'zoom-simulation' ? 'Zoom Simulation' : 
               sessionType === 'demo-simulation' ? 'Demo Simulation' : 
               'Active Session'}
            </div>
          </div>
        </div>
        {sessionType !== 'text-simulation' && sessionType !== 'demo-simulation' && (
          <div className="mt-2 text-sm text-gray-500">{zoomUrl}</div>
        )}
      </header>

      {/* Main content - split panels */}
      <div className="flex flex-1 overflow-hidden">
        <TranscriptionPanel transcription={transcription} />
        <AlertsPanel alerts={alerts} />
      </div>
    </div>
  )
}

export default MonitoringInterface