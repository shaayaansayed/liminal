---
url: "https://docs.recall.ai/docs/real-time-webhook-endpoints"
title: "Real-Time Webhook Endpoints"
---

Real-time webhook endpoints allow you to subscribe to a variety of participant events.

These are particularly useful for creating real-time experiences by triggering logic on your server when specific user actions are taken.

# Event Types   [Skip link to Event Types](https://docs.recall.ai/docs/real-time-webhook-endpoints\#event-types)

Real-time webhook endpoints can subscribe to all of the following events:

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

# Setup & Configuration   [Skip link to Setup & Configuration](https://docs.recall.ai/docs/real-time-webhook-endpoints\#setup--configuration)

## Bots   [Skip link to Bots](https://docs.recall.ai/docs/real-time-webhook-endpoints\#bots)

To configure a [Create Bot](https://docs.recall.ai/reference/bot_create) request with a real-time webhook endpoint, you must provide a real-time endpoint object in the `recording_config.real_time_endpoints` array.

The object should have a `type` of `webhook` and a `config` object specifying a `url` and `events`:

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "meeting_url": "https://meet.google.com/hzj-adhd-inu",
  "recording_config": {
    "realtime_endpoints": [\
      {\
        "type": "webhook",\
        "url": "https://my-app.com/api/webhook/recall",\
        "events": ["participant_events.join", "participant_events.leave"]\
      }\
    ]
  }
}
'

```

In the above example, we configure real-time endpoint which will receive the `participant_events.join` and `participant_events.leave` events at the following URL: [https://my-app.com/api/webhook/recall](https://my-app.com/api/webhook/recall)

> ## 📘  Realtime Webhooks Are Not Configurable Via Dashboard
>
> Realtime webhook endpoints are dispatched directly to the provided URL in the Create Bot request. These must be provided on a per bot basis and cannot be configured in the Webhooks dashboard

# Verification   [Skip link to Verification](https://docs.recall.ai/docs/real-time-webhook-endpoints\#verification)

Since your webhook receiver must be accessible at a publicly exposed endpoint, you should add a verification mechanism to ensure you only process requests coming from Recall.

To do this, you should provide a secret or token as a query parameter in the endpoint's URL, such as `token=some-random-token`.

When we make the request to your endpoint, we will use the **exact** url, including any query parameters. You will then be able to verify the query parameter in your server's webhook handler, and reject any requests that do not contain your secret/token value.

# Retry Policy   [Skip link to Retry Policy](https://docs.recall.ai/docs/real-time-webhook-endpoints\#retry-policy)

Realtime webhook messages are automatically retried by Recall based on the following policy:

**Retry condition**: We retry if the HTTP POST request to the provided URL fails due to:

- Network errors (e.g., connection timeouts)
- Non-successful HTTP status codes (i.e., not in the `2xx` range)

**Retry limit**: A maximum of **60 retry attempts** are made per webhook event.

**Backoff strategy**: Retries are attempted with a **fixed 1-second interval** between attempts.

**Dropping behavior**: Once **60 failed attempts** are reached, the realtime endpoint is marked as `failed` and no further messages are delivered

Updated 15 days ago

* * *

Did this page help you?

Yes

No

Ask AI