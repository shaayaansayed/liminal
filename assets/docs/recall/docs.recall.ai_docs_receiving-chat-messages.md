---
url: "https://docs.recall.ai/docs/receiving-chat-messages"
title: "Receiving Chat Messages"
---

# Platform Support   [Skip link to Platform Support](https://docs.recall.ai/docs/receiving-chat-messages\#platform-support)

| Platform | Supported | Limitations |
| --- | --- | --- |
| Zoom | ✅ | Receiving chat messages in the [Zoom Native Bot](https://docs.recall.ai/docs/zoom-native-bots) is not currently supported |
| Google Meet | ✅ |  |
| Microsoft Teams | ✅ | Bots can only receive chat messages if the meeting chat is accessible to anonymous participants. |
| Cisco Webex | ❌ |  |
| Slack Huddles | ❌ |  |

# Setup & Configuration   [Skip link to Setup & Configuration](https://docs.recall.ai/docs/receiving-chat-messages\#setup--configuration)

To receive chat message webhooks, set a [Real-Time Webhook Endpoint](https://docs.recall.ai/docs/real-time-webhook-endpoints) with the `participant_events.chat_message` event when calling [Create Bot](https://docs.recall.ai/reference/bot_create):

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "meeting_url": "https://meet.google.com/hzj-adhd-inu",
  "recording_config": {
    "realtime_endpoints": [\
      {\
        "type": "webhook",\
        "url": "https://my-app.com/api/webhook/recall",\
        "events": ["participant_events.chat_message"]\
      }\
    ]
  }
}
'

```

Then, **as long as the bot is in the `in_call_recording` state**, the configured endpoint will receive chat messages as webhook events.

# Event Payload   [Skip link to Event Payload](https://docs.recall.ai/docs/receiving-chat-messages\#event-payload)

Whenever a message readable by the bot is received in the chat, your endpoint will receive a webhook event with the following payload:

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

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI