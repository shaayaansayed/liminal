import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom'
import JoinSession from './pages/JoinSession'
import MonitoringInterface from './pages/MonitoringInterface'

export function App() {
  const [isSessionActive, setIsSessionActive] = useState(false)
  const [sessionInfo, setSessionInfo] = useState<{
    url: string
    type: 'real' | 'zoom-simulation' | 'text-simulation' | 'demo-simulation'
  } | null>(null)
  
  const handleJoinSession = (url: string, sessionType?: 'real' | 'zoom-simulation' | 'text-simulation' | 'demo-simulation') => {
    // Use provided session type or determine from URL
    const type = sessionType || (url === 'text-based-simulation' ? 'text-simulation' : 'real')
    
    setSessionInfo({ url, type })
    setIsSessionActive(true)
  }
  
  return (
    <Router>
      <div className="w-full min-h-screen bg-gray-50">
        <Routes>
          <Route
            path="/"
            element={<JoinSession onJoinSession={handleJoinSession} />}
          />
          <Route
            path="/monitoring"
            element={
              isSessionActive && sessionInfo ? (
                <MonitoringInterface 
                  zoomUrl={sessionInfo.url} 
                  sessionType={sessionInfo.type}
                />
              ) : (
                <Navigate to="/" />
              )
            }
          />
        </Routes>
      </div>
    </Router>
  )
}

export default App