// API configuration
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export { API_BASE_URL };

// Types
export interface TranscriptWord {
  text: string;
  start_timestamp: number;
  end_timestamp: number | null;
}

export interface TranscriptSegment {
  participant_id: string;
  participant_name: string;
  is_partial: boolean;
  words: TranscriptWord[];
  timestamp: string;
}

export interface TranscriptResponse {
  transcript: TranscriptSegment[];
  segment_count: number;
}

export interface FormattedTranscriptResponse {
  transcript: string;
  segment_count: number;
}

// API client utility
export class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;

    const response = await fetch(url, {
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  // API methods
  async getHealth() {
    return this.request("/health");
  }

  async startSession(params: {
    sessionType: 'real' | 'simulation';
    isTextBased: boolean;
    meetingUrl: string | null;
    demoId?: string;
  }) {
    return this.request("/api/session", {
      method: "POST",
      body: JSON.stringify({
        sessionType: params.sessionType,
        isTextBased: params.isTextBased,
        meetingUrl: params.meetingUrl,
        ...(params.demoId && { demoId: params.demoId })
      }),
    });
  }

  async resetSession() {
    return this.request("/api/reset-session", {
      method: "POST",
    });
  }

  // Transcript methods
  async getTranscript(format: "json" | "text" = "json", lastSeconds?: number) {
    let endpoint = `/api/transcript?format=${format}`;
    if (lastSeconds !== undefined) {
      endpoint += `&last_seconds=${lastSeconds}`;
    }
    
    if (format === "json") {
      return this.request<TranscriptResponse>(endpoint);
    } else {
      return this.request<FormattedTranscriptResponse>(endpoint);
    }
  }

  async getLatestTranscript(seconds: number = 30) {
    return this.request<TranscriptResponse & { seconds: number }>(
      `/api/transcript/latest?seconds=${seconds}`
    );
  }

  async getUsers() {
    return this.request("/api/users");
  }

  async getUser(id: number) {
    return this.request(`/api/users/${id}`);
  }

  async getRoot() {
    return this.request("/");
  }
}

// Default export for easy usage
export const apiClient = new ApiClient();