import React from 'react'
import {
  AlertCircleIcon,
  ClockIcon,
  BrainIcon,
  MessageSquareIcon,
  UserIcon,
  InfoIcon,
} from 'lucide-react'

interface Alert {
  id: string
  type: string
  message: string
  timestamp: string
}

interface AlertsPanelProps {
  alerts: Alert[]
}

const AlertsPanel: React.FC<AlertsPanelProps> = ({ alerts }) => {
  const getAlertIcon = (type: string) => {
    switch (type) {
      case 'silence':
        return <ClockIcon className="h-5 w-5 text-yellow-500" />
      case 'pace_too_fast':
        return <ClockIcon className="h-5 w-5 text-orange-500" />
      case 'emotion':
        return <AlertCircleIcon className="h-5 w-5 text-red-500" />
      case 'keyword':
        return <MessageSquareIcon className="h-5 w-5 text-blue-500" />
      case 'recommendation':
        return <BrainIcon className="h-5 w-5 text-green-500" />
      case 'info':
        return <InfoIcon className="h-5 w-5 text-blue-500" />
      case 'participant':
        return <UserIcon className="h-5 w-5 text-purple-500" />
      default:
        return <AlertCircleIcon className="h-5 w-5 text-gray-500" />
    }
  }

  const getAlertBackground = (type: string) => {
    switch (type) {
      case 'silence':
        return 'bg-yellow-50 border-yellow-200'
      case 'pace_too_fast':
        return 'bg-orange-50 border-orange-200'
      case 'emotion':
        return 'bg-red-50 border-red-200'
      case 'keyword':
        return 'bg-blue-50 border-blue-200'
      case 'recommendation':
        return 'bg-green-50 border-green-200'
      case 'info':
        return 'bg-blue-50 border-blue-200'
      case 'participant':
        return 'bg-purple-50 border-purple-200'
      default:
        return 'bg-gray-50 border-gray-200'
    }
  }

  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp)
    return date.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
    })
  }

  // Show only the most recent 20 alerts
  const recentAlerts = alerts.slice(-20).reverse()

  return (
    <div className="w-1/3 bg-white overflow-hidden flex flex-col">
      <div className="px-6 py-3 border-b border-gray-200 flex justify-between items-center">
        <h2 className="font-medium text-lg text-gray-800">Real-Time Alerts</h2>
        {alerts.length > 0 && (
          <span className="text-sm text-gray-500">
            {alerts.length} total
          </span>
        )}
      </div>
      <div className="flex-1 overflow-y-auto p-4">
        <div className="space-y-3">
          {recentAlerts.length > 0 ? (
            recentAlerts.map((alert) => (
              <div
                key={alert.id}
                className={`p-3 rounded-lg border transition-all duration-300 ${getAlertBackground(alert.type)}`}
              >
                <div className="flex items-start">
                  <div className="mr-3 mt-0.5">{getAlertIcon(alert.type)}</div>
                  <div className="flex-1">
                    <p className="text-gray-800 text-sm">{alert.message}</p>
                    <p className="text-xs text-gray-500 mt-1">
                      {formatTime(alert.timestamp)}
                    </p>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div className="text-center py-8 text-gray-500">
              No alerts yet
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default AlertsPanel