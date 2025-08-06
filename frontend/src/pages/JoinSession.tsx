import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowRightIcon } from 'lucide-react'
import { apiClient } from '../config/api'

interface JoinSessionProps {
  onJoinSession: (url: string, sessionType?: 'real' | 'zoom-simulation' | 'text-simulation' | 'demo-simulation') => void
}

const JoinSession: React.FC<JoinSessionProps> = ({ onJoinSession }) => {
  const [zoomUrl, setZoomUrl] = useState('')
  const [error, setError] = useState('')
  const [sessionType, setSessionType] = useState<'real' | 'simulation'>('real')
  const [isTextBased, setIsTextBased] = useState(false)
  const [selectedDemo, setSelectedDemo] = useState<string>('')
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    // Skip Zoom URL validation for text-based simulation
    if (
      (sessionType === 'real' ||
        (sessionType === 'simulation' && !isTextBased)) &&
      !zoomUrl.trim()
    ) {
      setError('Please enter a Zoom URL')
      return
    }
    
    if (
      (sessionType === 'real' ||
        (sessionType === 'simulation' && !isTextBased)) &&
      !zoomUrl.includes('zoom.us')
    ) {
      setError('Please enter a valid Zoom URL')
      return
    }

    try {
      // Create payload for unified API call
      const payload = {
        sessionType: sessionType,
        isTextBased: isTextBased,
        meetingUrl: isTextBased ? null : zoomUrl,
        demoId: selectedDemo || undefined
      }
      
      // Make single API call
      const response = await apiClient.startSession(payload)
      console.log('Session started:', response)
      
      // Determine session type for navigation
      const navigationType = sessionType === 'real' ? 'real' : 
                           (selectedDemo ? 'demo-simulation' : 
                            (isTextBased ? 'text-simulation' : 'zoom-simulation'))
      
      // Navigate to monitoring page
      onJoinSession(
        sessionType === 'simulation' && isTextBased ? 'text-based-simulation' : zoomUrl,
        navigationType
      )
      navigate('/monitoring')
    } catch (error) {
      setError('Failed to start session. Please try again.')
      console.error('Session start error:', error)
    }
  }

  const showZoomUrlInput =
    sessionType === 'real' || (sessionType === 'simulation' && !isTextBased)

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-white">
      <div className="w-full max-w-md">
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            Behavioral Health Copilot
          </h1>
          <p className="text-gray-600">Join a session to begin monitoring</p>
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Session Type Selection */}
          <div className="space-y-2">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Session Type
            </label>
            <div className="flex bg-gray-100 p-1 rounded-lg">
              <button
                type="button"
                onClick={() => setSessionType('real')}
                className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                  sessionType === 'real'
                    ? 'bg-white shadow-sm text-blue-700'
                    : 'text-gray-700 hover:text-gray-900'
                }`}
              >
                Real Session
              </button>
              <button
                type="button"
                onClick={() => setSessionType('simulation')}
                className={`flex-1 py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                  sessionType === 'simulation'
                    ? 'bg-white shadow-sm text-blue-700'
                    : 'text-gray-700 hover:text-gray-900'
                }`}
              >
                Simulation
              </button>
            </div>
          </div>
          
          {/* Simulation Options (only for Simulation) */}
          {sessionType === 'simulation' && (
            <>
              {/* Demo Selection */}
              <div className="space-y-2">
                <label htmlFor="demo-select" className="block text-sm font-medium text-gray-700">
                  Demo Scenario
                </label>
                <select
                  id="demo-select"
                  value={selectedDemo}
                  onChange={(e) => setSelectedDemo(e.target.value)}
                  className="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="">Live LLM Simulation</option>
                  <option value="fast_pace_demo">Demo: Fast Paced Conversation</option>
                  <option value="reflective_demo">Demo: Reflective Conversation</option>
                </select>
              </div>

              {/* Text-Based Simulation Checkbox */}
              <div className="flex items-center">
                <input
                  id="text-based"
                  type="checkbox"
                  checked={isTextBased}
                  onChange={(e) => setIsTextBased(e.target.checked)}
                  className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
                <label
                  htmlFor="text-based"
                  className="ml-2 block text-sm text-gray-700"
                >
                  Text-Based Simulation
                </label>
              </div>
            </>
          )}
          
          {/* Zoom URL Input (conditionally shown) */}
          {showZoomUrlInput && (
            <div className="space-y-2">
              <label
                htmlFor="zoom-url"
                className="block text-sm font-medium text-gray-700"
              >
                Zoom Meeting URL
              </label>
              <input
                id="zoom-url"
                type="text"
                value={zoomUrl}
                onChange={(e) => {
                  setZoomUrl(e.target.value)
                  setError('')
                }}
                placeholder="https://zoom.us/j/123456789"
                className="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              {error && <p className="text-sm text-red-600">{error}</p>}
            </div>
          )}
          
          {/* Action Button */}
          <button
            type="submit"
            className="w-full flex items-center justify-center px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-md transition-colors"
          >
            {sessionType === 'real' ? 'Start Monitoring' : 'Start Simulation'}
            <ArrowRightIcon className="ml-2 h-4 w-4" />
          </button>
        </form>
      </div>
    </div>
  )
}

export default JoinSession