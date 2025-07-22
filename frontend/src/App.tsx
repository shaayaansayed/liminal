import { useState, useEffect, useRef } from "react";
import { API_BASE_URL } from "./config/api";

interface Alert {
  id: string;
  participant: string;
  participant_id: string;
  silent_duration: number;
  timestamp: string;
}

function AlertComponent({ alert, onDismiss }: { alert: Alert; onDismiss: (id: string) => void }) {
  useEffect(() => {
    const timer = setTimeout(() => {
      onDismiss(alert.id);
    }, 5000); // Auto-dismiss after 5 seconds

    return () => clearTimeout(timer);
  }, [alert.id, onDismiss]);

  return (
    <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-2 shadow-lg">
      <div className="flex justify-between items-center">
        <div>
          <strong className="font-bold">🔇 Silence Alert!</strong>
          <span className="block sm:inline"> {alert.participant} hasn't spoken for {alert.silent_duration} seconds</span>
        </div>
        <button 
          onClick={() => onDismiss(alert.id)}
          className="text-red-500 hover:text-red-700 font-bold text-lg"
        >
          ×
        </button>
      </div>
    </div>
  );
}

function TestBotCreation() {
  const [meetingUrl, setMeetingUrl] = useState("");
  const [result, setResult] = useState(null);

  const createBot = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/create-bot`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ meeting_url: meetingUrl })
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: error.message });
    }
  };

  return (
    <div className="bg-gray-50 dark:bg-gray-800/50 p-6 rounded-lg mb-6">
      <h2 className="text-xl font-semibold mb-4">Test Bot Creation</h2>
      <div className="mb-4">
        <input 
          value={meetingUrl} 
          onChange={(e) => setMeetingUrl(e.target.value)}
          placeholder="Zoom meeting URL" 
          className="w-full p-3 border border-gray-300 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white"
        />
      </div>
      <button 
        onClick={createBot}
        className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors mb-4"
      >
        Create Bot
      </button>
      {result && (
        <div className="mt-4">
          <pre className="bg-gray-900 text-white p-4 rounded-lg overflow-auto text-left text-sm">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

function App() {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [wsStatus, setWsStatus] = useState<string>("Disconnected");
  const ws = useRef<WebSocket | null>(null);

  // WebSocket connection management
  useEffect(() => {
    const connectWebSocket = () => {
      const wsUrl = API_BASE_URL.replace('http', 'ws') + '/ws/alerts';
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
            // Add new alert
            const newAlert: Alert = {
              id: `${message.participant_id}-${Date.now()}`,
              participant: message.participant,
              participant_id: message.participant_id,
              silent_duration: message.silent_duration,
              timestamp: message.timestamp
            };
            
            setAlerts(prev => [...prev, newAlert]);
            console.log('Silence alert added:', newAlert);
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

  const dismissAlert = (alertId: string) => {
    setAlerts(prev => prev.filter(alert => alert.id !== alertId));
  };

  return (
    <div className="max-w-5xl mx-auto p-8">
      {/* WebSocket Status */}
      <div className="mb-4 text-sm">
        <span className={`inline-block px-2 py-1 rounded ${
          wsStatus === 'Connected' ? 'bg-green-100 text-green-800' :
          wsStatus === 'Error' ? 'bg-red-100 text-red-800' :
          'bg-gray-100 text-gray-800'
        }`}>
          WebSocket: {wsStatus}
        </span>
      </div>

      {/* Alerts Container */}
      {alerts.length > 0 && (
        <div className="mb-6">
          <h3 className="text-lg font-semibold mb-2">🚨 Active Alerts</h3>
          {alerts.map(alert => (
            <AlertComponent 
              key={alert.id} 
              alert={alert} 
              onDismiss={dismissAlert}
            />
          ))}
        </div>
      )}


      {/* Bot Creation Component */}
      <div className="text-center">
        <TestBotCreation />
      </div>
    </div>
  );
}

export default App;
