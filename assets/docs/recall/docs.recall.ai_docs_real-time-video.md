---
url: "https://docs.recall.ai/docs/real-time-video"
title: "Receive Real-Time Video: Websockets"
---

> ## 📘
>
> Video websockets are optimized for those doing real-time AI video analysis, providing 360p PNG image frames at 2fps.
>
> If you're looking to receive real time video for human consumption instead, refer to [Real-time Video: RTMP](https://docs.recall.ai/docs/stream-real-time-video-rtmp) guide.

# Quickstart   [Skip link to Quickstart](https://docs.recall.ai/docs/real-time-video\#quickstart)

* * *

To receive raw audio in real-time from a bot, you can leverage [Real-Time Websocket Endpoints](https://docs.recall.ai/docs/real-time-websocket-endpoints).

## Setup a websocket endpoint   [Skip link to Setup a websocket endpoint](https://docs.recall.ai/docs/real-time-video\#setup-a-websocket-endpoint)

For demonstration purposes, we've set up a simple websocket receiver to receive and write audio to a file:

TypeScript

```rdmd-code lang-typescript theme-light

import WebSocket from 'ws';
import fs from 'fs';

type AudioDataEvent = {
  event: 'video_separate_png.data';
  data: {
    data: {
      buffer: string, // base64 encoded png
      timestamp: {
      	relative: float,
        absolute: string
    	},
      type: string // "webcam" | "screenshare",
      participant: {
      	id: number,
      	name: string | null,
        is_host: boolean,
        platform: string | null,
        extra_data: object
      }
    },
    realtime_endpoint: {
      id: string;
      metadata: Record<string, string>;
    },
    recording: {
      id: string;
      metadata: Record<string, string>;
    },
    bot: {
      id: string;
      metadata: Record<string, string>;
    },
    audio_mixed_raw: {
      id: string;
      metadata: Record<string, string>;
    }
  };
};

const wss = new WebSocket.Server({ port: 3456 });

wss.on('connection', (ws) => {
  ws.on('message', (message: WebSocket.Data) => {
    console.log(message);

    // You can listen to the audio using this command:
    // ffmpeg -f s16le -ar 16000 -ac 1 -i /tmp/{RECORDING_ID}.bin -c:a libmp3lame -q:a 2 /tmp/{RECORDING_ID}.mp3
    try {
      const wsMessage = JSON.parse(message.toString()) as AudioDataEvent;

      if (wsMessage.event === 'video_separate_png.data') {
        console.log(wsMessage);

        // Use the recording ID for the file name
        const recordingId = wsMessage.data.recording.id;
        const filePath = `/tmp/${recordingId}.bin`;

        const encodedBuffer = Buffer.from(wsMessage.data.data.buffer, 'base64');
        const decodedBuffer = Buffer.from(encodedBuffer, 'utf8');
        fs.appendFileSync(filePath, decodedBuffer);
      } else {
        console.log("unhandled message", wsMessage.event);
      }
    } catch (e) {
      console.error('Error parsing JSON:', e);
    }
  });

  ws.on('error', (error) => {
    console.error('WebSocket Error:', error);
  });

  ws.on('close', () => {
    console.log('WebSocket Closed');
  });
});

console.log('WebSocket server started on port 3456');

```

For details on how to verify connections, see [Verifying Real-Time Websocket Endpoints](https://docs.recall.ai/docs/real-time-websocket-endpoints#verification).

Once you have a basic server running locally, you'll want to expose it publicly through a tunneling tool such as [ngrok](https://ngrok.com/). For a full setup guide, see [Local Webhook Development](https://docs.recall.ai/docs/local-webhook-development).

## Start a meeting   [Skip link to Start a meeting](https://docs.recall.ai/docs/real-time-video\#start-a-meeting)

Now that we have our websocket server running locally and exposed through our ngrok tunnel, it's time to start a meeting and send a bot to it.

For simplicity, go to [meet.new](https://meet.new/) in a new tab to start an instant Google Meet call. Save this URL for the next step.

## Configure the bot   [Skip link to Configure the bot](https://docs.recall.ai/docs/real-time-video\#configure-the-bot)

Now it's time to send a bot to a meeting while configuring a real-time websocket endpoint.

To do this, call the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint while providing a real-time endpoint object where:

- **`type`:** `websocket`
- **`config.url`:** Your publicly exposed ngrok tunnel URL
- **`config.events`:** An array including the `video_separate_png.data` event

To get separate video per participant, `recording_config.video_mixed_layout` to **gallery\_view\_v2**. And of course, don't forget to set `meeting_url` to your newly-created Google Meet call.

**Example curl:**

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "meeting_url": "https://meet.google.com/sde-zixx-iry",
  "recording_config": {
    "video_separate_png": {},
    "video_mixed_layout": "gallery_view_v2",
    "realtime_endpoints": [\
      {\
        "type": "websocket",\
        "config": {\
          "url": "wss://my-tunnel-domain.ngrok-free.app",\
          "events": ["video_separate_png.data"]\
        }\
      }\
    ]
  }
}
'

```

> ## 📘
>
> Make sure to set the `config.url` as a `ws` or `wss` endpoint.

## Receive video frames   [Skip link to Receive video frames](https://docs.recall.ai/docs/real-time-video\#receive-video-frames)

Once the bot is on the call and connected to audio, it will begin producing `video_separate_png.data` events containing packets base64 encoded png frames

These events have the following shape:

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

# Image Frame Dimensions   [Skip link to Image Frame Dimensions](https://docs.recall.ai/docs/real-time-video\#image-frame-dimensions)

`data.buffer` is the b64-encoded png frame. The dimensions for the PNG images are the same for all meeting platforms.

| Video stream | Image Dimensions |
| --- | --- |
| Participant - Default | 480x360 |
| Participant - While screensharing | 480x360 |
| Screenshare | 1280×720 |

> ## 🎉
>
> And that's it! You're now streaming video in real-time to a websocket server.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/real-time-video\#faq)

* * *

## What is the retry behavior?   [Skip link to What is the retry behavior?](https://docs.recall.ai/docs/real-time-video\#what-is-the-retry-behavior)

If we are unable to connect to your endpoint, or are disconnected, we will re-try the connection every 3 seconds, while the bot is alive.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI