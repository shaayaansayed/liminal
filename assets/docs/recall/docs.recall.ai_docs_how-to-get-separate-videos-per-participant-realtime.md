---
url: "https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime"
title: "How to get Separate Videos per Participant (Realtime)"
---

> ## 📘  Video data streaming is currently supported in only png format

This guide is for you if:

- You want to process video data for each participant in realtime

### Platforms Support   [Skip link to Platforms Support](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime\#platforms-support)

| Platform |  |
| --- | --- |
| Zoom | ✅ |
| Microsoft Teams | ✅ |
| Google Meet | ✅ |
| Webex | ❌ |
| Slack Huddles (Beta) | ✅ |
| Go-To Meeting (Beta) | ✅ |

### Recording Specifications   [Skip link to Recording Specifications](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime\#recording-specifications)

|  | Resolution | Frame Rate |
| --- | --- | --- |
| Screen Share Video | 360p | 2 frames per second |
| Participant Video | 360p | 2 frames per second |

# Implementation   [Skip link to Implementation](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime\#implementation)

## Step 1: Create a bot   [Skip link to Step 1: Create a bot](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime\#step-1-create-a-bot)

To get separate video per participant, you must set `recording_config.video_mixed_layout = "gallery_view_v2"`. Below is an example of what it would look like in your request

cURLTypeScriptPython

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: YOUR_RECALL_API_KEY' \
     --data '
{
  "meeting_url": "YOUR_MEETING_URL",
  "recording_config": {
    "video_mixed_layout": "gallery_view_v2", # Add this to your request body
    "video_separate_png": {} # Add this to your request body,
    "realtime_endpoints": [\
      {\
      	type: "websocket", // only websocket is supported for realtime video data\
        url: YOUR_WEBSOCKET_RECEIVER_URL,\
        events: ["video_separate_png.data"]\
      }\
    ]
  }
}
'

```

```rdmd-code lang-typescript theme-light

const response = await fetch("https://us-east-1.recall.ai/api/v1/bot", {
  method: "POST",
  headers: {
    "accept": "application/json",
    "content-type": "application/json"
    "authorization": "YOUR_RECALL_API_KEY" // Update this
  },
  body: JSON.stringify({
    meeting_url: "YOUR_MEETING_URL", // Update this
    recording_config: {
      video_mixed_layout: "gallery_view_v2", // Add this to your request body
      video_separate_mp4: {} # Add this to your request body
    }
  })
});

if (!response.ok) {
  throw new Error(`Error: ${response.status} ${response.statusText}`);
}

const data = await response.json();

```

```rdmd-code lang-python theme-light

import requests

response = requests.post(
    "https://us-east-1.recall.ai/api/v1/bot",
    json={
      "meeting_url": "YOUR_MEETING_URL", # Update this
      "recording_config": {
	      "video_mixed_layout": "gallery_view_v2" # Add this to your request body
		    "video_separate_mp4": {} # Add this to your request body
      }
    },
    headers={
      "accept": "application/json",
      "content-type": "application/json",
    	"authorization": "YOUR_RECALL_API_KEY" # Update this
    }
)

if not response.ok:
 	errorMessage = f"Error: {response.status_code} - {response.text}"
  raise requests.RequestException(errorMessage)

result = response.json()

```

## Step 2: Receive websocket messages with video data   [Skip link to Step 2: Receive websocket messages with video data](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-realtime\#step-2-receive-websocket-messages-with-video-data)

Setup a websocket server and ensure it is publicly accessible. You will receive messages in the following payload format:

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