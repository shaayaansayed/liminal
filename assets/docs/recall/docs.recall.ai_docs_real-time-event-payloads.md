---
url: "https://docs.recall.ai/docs/real-time-event-payloads"
title: "Real-Time Event Payloads"
---

# `participant_events`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#participant_events)

JSON

```rdmd-code lang-json theme-light

{
  "event": "participant_events.chat_message", // participant_events.join, participant_events.leave, participant_events.speech_on, participant_events.speech_off (& more)
  "data": {
    "data": {
      "participant": {
      	"id": number,
      	"name": string | null,
        "is_host": boolean,
        "platform": string | null,
        "extra_data": object
    	},
      "timestamp": {
        "absolute": string,
        "relative": float
      },
      "data":
      	{
          "text": string,
          "to": string
        } // populated for `participant_events.chat_message` event
      	| null
    },
    // The real-time endpoint configured to receive data
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    // The associated ParticipantEvents Resource encapsulating this data
    "participant_events": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    // The related bot, if the recording is produced by a bot
    "bot": {
      "id": string,
      "metadata": object
    }
  }
}

```

# `transcript.data`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#transcriptdata)

JSON

```rdmd-code lang-json theme-light

{
  "event": "transcript.data",
  "data": {
    "data": {
      "words": [{\
        "text": string,\
        "start_timestamp": { "relative": float },\
        "end_timestamp": {"relative": float } | null\
      }],
      "participant": {
      	"id": number,
      	"name": string | null,
        "is_host": boolean,
        "platform": string | null,
        "extra_data": object
      }
    },
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    "transcript": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    "bot": {
      "id": string,
      "metadata": object
    }
  }
}

```

# `transcript.partial_data`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#transcriptpartial_data)

JSON

```rdmd-code lang-json theme-light

{
  "event": "transcript.partial_data",
  "data": {
    "data": {
      "words": [{\
        "text": string,\
        "start_timestamp": { "relative": float },\
        "end_timestamp": {"relative": float } | null\
      }],
      "participant": {
      	"id": number,
      	"name": string | null,
        "is_host": boolean,
        "platform": string | null,
        "extra_data": object
      }
    },
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    "transcript": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    "bot": {
      "id": string,
      "metadata": object
    }
  }
}

```

# `audio_mixed_raw.data`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#audio_mixed_rawdata)

JSON

```rdmd-code lang-json theme-light

{
  "event": "audio_mixed_raw.data",
  "data": {
    "data": {
      "buffer": string, // base64-encoded raw audio 16 kHz mono, S16LE(16-bit PCM LE)
      "timestamp": {
      	"relative": float,
        "absolute": string
    	}
    },
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    "audio_mixed": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    "bot": {
      "id": string,
      "metadata": object
    },
  }
}

```

# `audio_separate_raw.data`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#audio_separate_rawdata)

JSON

```rdmd-code lang-json theme-light

{
  "event": "audio_separate_raw.data",
  "data": {
    "data": {
      "buffer": string, // base64-encoded raw audio 16 kHz mono, S16LE(16-bit PCM LE)
      "timestamp": {
      	"relative": float,
        "absolute": string
    	},
      "participant": {
      	"id": number,
      	"name": string | null,
        "is_host": boolean,
        "platform": string | null,
        "extra_data": object
      }
    },
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    "audio_separate": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    "bot": {
      "id": string,
      "metadata": object
    },
  }
}

```

# `video_separate_png.data`   [Skip link to [object Object]](https://docs.recall.ai/docs/real-time-event-payloads\#video_separate_pngdata)

JSON

```rdmd-code lang-json theme-light

{
  "event": "video_separate_png.data",
  "data": {
    "data": {
      "buffer": string, // base64 encoded png at 2fps with resolution 360x640
      "timestamp": {
      	"relative": float,
        "absolute": string
    	},
      "type": "webcam" | "screenshare",
      "participant": {
      	"id": number,
      	"name": string | null,
        "is_host": boolean,
        "platform": string | null,
        "extra_data": object
      }
    },
    "realtime_endpoint": {
      "id": string,
      "metadata": object,
    },
    "video_separate": {
      "id": string,
      "metadata": object
    },
    "recording": {
      "id": string,
      "metadata": object
    },
    "bot": {
      "id": string,
      "metadata": object
    },
  }
}

```

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI