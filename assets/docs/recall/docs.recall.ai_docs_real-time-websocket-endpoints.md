---
url: "https://docs.recall.ai/docs/real-time-websocket-endpoints"
title: "Real-Time Websocket Endpoints"
---

In addition to [Webhooks](https://docs.recall.ai/docs/real-time-webhook-endpoints), Recall.ai supports receiving data in real-time via a websocket connection.

You can register a websocket real-time endpoint during data source creation (for instance, when [Creating a Bot](https://docs.recall.ai/reference/bot_create), specifying the specific events you want to receive.

# Event Types   [Skip link to Event Types](https://docs.recall.ai/docs/real-time-websocket-endpoints\#event-types)

Real-time websocket endpoints can subscribe to all of the following events:

| Event | Description | Payload |
| --- | --- | --- |
| `participant_events.join` | A participant joined. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.leave` | A participant left. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.update` | A participant updated their details. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.speech_on` | A participant started speaking. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.speech_off` | A participant stopped speaking. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.webcam_on` | A participant turned on their webcam. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.webcam_off` | A participant turned off their webcam. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.screenshare_on` | A participant started screen sharing. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.screenshare_off` | A participant stopped screen sharing. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `participant_events.chat_message` | A participant sent a chat message. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) |
| `transcript.data` | A transcript utterance was generated (see [Real-time Transcription](https://docs.recall.ai/docs/real-time-transcription) | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#transcriptdata) |
| `audio_mixed_raw.data` | A mixed audio buffer was generated from the call. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#audio_mixed_rawdata) |
| `audio_separate_raw.data` | A separate audio buffer was generated from the call. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#audio_separate_rawdata) |
| `video_separate_png.data` | A separate video buffer was generated from the call. | [Schema](https://docs.recall.ai/docs/real-time-event-payloads#video_separate_pngdata) |

# Setup & Configuration   [Skip link to Setup & Configuration](https://docs.recall.ai/docs/real-time-websocket-endpoints\#setup--configuration)

* * *

## Bots   [Skip link to Bots](https://docs.recall.ai/docs/real-time-websocket-endpoints\#bots)

To configure a real-time websocket endpoint for a bot, add a real time endpoint to your [Create Bot](https://docs.recall.ai/reference/bot_create) request with the `type` set to `websocket`:

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
	  "realtime_endpoints": [\
      {\
        "type": "websocket",\
        "url": "wss://my-app.com/api/ws/audio",\
        "events": ["audio_mixed_raw.data"]\
      }\
    ]
  }
}
'

```

The above request creates a bot and registers a real-time websocket endpoint to receive `audio_mixed_raw.data` events at the following URL: `wss://my-app.com/api/ws/audio`

> ## 📘
>
> The `config.url` must be either a `ws` or `wss` endpoint.

# Verification   [Skip link to Verification](https://docs.recall.ai/docs/real-time-websocket-endpoints\#verification)

Since your websocket receiver must be accessible at a publicly exposed URL, you must add a verification mechanism to ensure you only accept connections coming from Recall.

To do this, provide a secret or token as a query parameter in the endpoint's URL, such as `token=some-random-token`.

When we make the request to connect to your endpoint, we will use the **exact** url, including any query parameters. You will then be able to verify the query parameter in your server's websocket handler, and reject any requests that do not contain your secret/token value.

# Retry Policy   [Skip link to Retry Policy](https://docs.recall.ai/docs/real-time-websocket-endpoints\#retry-policy)

Recall attemps to maintain a persistent WebSocket connection and will retry automatically upon connection failure using the following policy:

**Retry condition**: A retry is triggered when the WebSocket connection fails due to:

- Network interruptions
- Server-side disconnects
- Failed connection handshake

**Retry limit**: A maximum of 30 retry attempts are made per connection failure incident.

**Backoff strategy**: Each retry is delayed by a fixed **3-second interval**.

**Dropping behavior**: If all **30 attempts fail**, the realtime endpoint is marked as `failed` and no further messages are delivered

Updated 15 days ago

* * *

Did this page help you?

Yes

No

Ask AI