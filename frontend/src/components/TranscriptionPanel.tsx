import React, { useEffect, useRef } from 'react'

interface TranscriptionEntry {
  id: number
  speaker: string
  text: string
  timestamp: string
  isPartial?: boolean
}

interface TranscriptionPanelProps {
  transcription: TranscriptionEntry[]
}

const TranscriptionPanel: React.FC<TranscriptionPanelProps> = ({
  transcription,
}) => {
  const transcriptionEndRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to bottom when new transcription entries appear
  useEffect(() => {
    if (transcriptionEndRef.current) {
      transcriptionEndRef.current.scrollIntoView({
        behavior: 'smooth',
      })
    }
  }, [transcription])

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp)
    return date.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    })
  }

  return (
    <div className="flex-1 border-r border-gray-200 bg-white overflow-hidden flex flex-col">
      <div className="px-6 py-3 border-b border-gray-200">
        <h2 className="font-medium text-lg text-gray-800">
          Live Transcription
        </h2>
      </div>
      <div className="flex-1 overflow-y-auto p-6">
        {transcription.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            Waiting for transcription data...
          </div>
        ) : (
          <div className="space-y-4">
            {transcription.map((entry) => (
              <div key={entry.id} className={`pb-3 ${entry.isPartial ? 'opacity-70' : ''}`}>
                <div className="flex items-start">
                  <div className="flex-shrink-0 mr-3">
                    <span
                      className={`inline-block px-2 py-1 text-xs rounded-full ${
                        entry.speaker === 'Therapist' 
                          ? 'bg-blue-100 text-blue-700' 
                          : 'bg-gray-100 text-gray-700'
                      }`}
                    >
                      {entry.speaker}
                    </span>
                  </div>
                  <div className="flex-1">
                    <p className={`text-gray-800 ${entry.isPartial ? 'italic' : ''}`}>
                      {entry.text}
                      {entry.isPartial && <span className="text-gray-400 text-sm ml-2">(speaking...)</span>}
                    </p>
                    <p className="text-xs text-gray-400 mt-1">
                      {formatTimestamp(entry.timestamp)}
                    </p>
                  </div>
                </div>
              </div>
            ))}
            <div ref={transcriptionEndRef} />
          </div>
        )}
      </div>
    </div>
  )
}

export default TranscriptionPanel