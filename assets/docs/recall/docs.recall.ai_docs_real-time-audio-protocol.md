---
url: "https://docs.recall.ai/docs/real-time-audio-protocol"
title: "Receive Real-Time Audio From Bot"
---

To receive raw audio in real-time from a bot, you can leverage [Real-Time Websocket Endpoints](https://docs.recall.ai/docs/real-time-websocket-endpoints).

# Quickstart   [Skip link to Quickstart](https://docs.recall.ai/docs/real-time-audio-protocol\#quickstart)

* * *

## Setup a websocket endpoint   [Skip link to Setup a websocket endpoint](https://docs.recall.ai/docs/real-time-audio-protocol\#setup-a-websocket-endpoint)

For demonstration purposes, we've set up a simple websocket receiver to receive and write audio to a file:

TypeScript

```rdmd-code lang-typescript theme-light

import WebSocket from 'ws';
import fs from 'fs';

type AudioDataEvent = {
  event: 'audio_mixed_raw.data';
  data: {
    data: {
      buffer: string; // Base64 encoded audio data
      timestamp: {
        relative: float;
        absolute: string;
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

      if (wsMessage.event === 'audio_mixed_raw.data') {
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

## Start a meeting   [Skip link to Start a meeting](https://docs.recall.ai/docs/real-time-audio-protocol\#start-a-meeting)

Now that we have our websocket server running locally and exposed through our ngrok tunnel, it's time to start a meeting and send a bot to it.

For simplicity, go to [meet.new](https://meet.new/) in a new tab to start an instant Google Meet call. Save this URL for the next step.

## Configure the bot   [Skip link to Configure the bot](https://docs.recall.ai/docs/real-time-audio-protocol\#configure-the-bot)

Now it's time to send a bot to a meeting while configuring a real-time websocket endpoint.

To do this, call the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint while providing a real-time endpoint object where:

- **`type`:** `websocket`
- **`url`:** Your publicly exposed ngrok tunnel URL
- **`events`:** An array including the `audio_mixed_raw.data` event

And of course, don't forget to set `meeting_url` to your newly-created Google Meet call.

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
    "audio_mixed_raw": {},
    "realtime_endpoints": [\
      {\
        "type": "websocket",\
        "url": "wss://my-tunnel-domain.ngrok-free.app",\
        "events": ["audio_mixed_raw.data"]\
      }\
    ]
  }
}
'

```

> ## 📘
>
> Make sure to set the `config.url` as a `ws` or `wss` endpoint.

## Receive the raw audio   [Skip link to Receive the raw audio](https://docs.recall.ai/docs/real-time-audio-protocol\#receive-the-raw-audio)

Once the bot is on the call and connected to audio, it will begin producing `audio_mixed_raw.data` events containing packets of mixed audio from the call.

These events have the following shape:

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

Where `data.buffer` is the b64-encoded mixed audio data. The data is mono 16 bit signed little-endian PCM at 16khz.

> ## 🎉
>
> And that's it! You're now streaming audio in real-time to a websocket server.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/real-time-audio-protocol\#faq)

* * *

## Do muted participants produce audio?   [Skip link to Do muted participants produce audio?](https://docs.recall.ai/docs/real-time-audio-protocol\#do-muted-participants-produce-audio)

No, muted participants do not produce any audio.

If a participant is _unmuted_ but silent, you will receive empty audio packets.

## Will bots receive audio from other bots?   [Skip link to Will bots receive audio from other bots?](https://docs.recall.ai/docs/real-time-audio-protocol\#will-bots-receive-audio-from-other-bots)

Since bots are participants, if there are other bots in a call, the bot will receive audio from the bot like any other participant.

Since bots are muted by default, unless another bot is [outputting audio](https://docs.recall.ai/reference/bot_output_audio_create), the bot will not receive audio packets from other bots.

## What is the retry behavior?   [Skip link to What is the retry behavior?](https://docs.recall.ai/docs/real-time-audio-protocol\#what-is-the-retry-behavior)

If we are unable to connect to your endpoint, or are disconnected, we will re-try the connection every 3 seconds, while the bot is alive.

Updated 19 days ago

* * *

Did this page help you?

Yes

No

Ask AI