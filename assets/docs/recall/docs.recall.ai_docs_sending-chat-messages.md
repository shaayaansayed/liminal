---
url: "https://docs.recall.ai/docs/sending-chat-messages"
title: "Sending Chat Messages"
---

# Platform Support   [Skip link to Platform Support](https://docs.recall.ai/docs/sending-chat-messages\#platform-support)

| Platform | Available | Supported Recipients | Limitations | Pinning |
| --- | --- | --- | --- | --- |
| Zoom | ✅ | `everyone`, `host`, `everyone_except_host` | 4096 character limit | ✅ |
| Google Meet | ✅ | `everyone` | 500 character limit | ✅ |
| Microsoft Teams | ✅ | `everyone` | 4096 character limit | ✅ (Bot must be signed-in) |
| Slack Huddles | ✅ | `everyone` |  | ❌ |
| Cisco Webex | ❌ |  |  | ❌ |

> ## 📘  Note about Microsoft Teams
>
> The Teams chat window may not be available for bots by default, due to the organization's settings.
>
> For bots to be able to send chat messages in Teams calls, they must have access to the chat. To have access to the chat, one of two things must happen:
>
> 1. The tenant has configured their meeting chat settings to allow **anyone** to chat.
> 2. The tenant allows authenticated users to chat **and** you're using [Signed-In Microsoft Teams Bots](https://docs.recall.ai/docs/microsoft-teams-bot-login).

# How to send chat messages   [Skip link to How to send chat messages](https://docs.recall.ai/docs/sending-chat-messages\#how-to-send-chat-messages)

There are two ways to have bots send chat messages:

1. **Providing an automatic chat configuration when [Creating a Bot](https://docs.recall.ai/reference/bot_create)**
2. **Calling the [Send Chat Message](https://docs.recall.ai/reference/bot_send_chat_message_create) endpoint**

## Providing an automatic chat configuration   [Skip link to Providing an automatic chat configuration](https://docs.recall.ai/docs/sending-chat-messages\#providing-an-automatic-chat-configuration)

* * *

When creating a bot, you can provide a `chat` object in the [Create Bot](https://docs.recall.ai/reference/bot_create) request body with two parameters that act as hooks for automatically sending chat messages:

- `on_bot_join`
- `on_participant_join`

_Note that you can provide one without the other, or both if you prefer._

### **Send a message when the bot joins: `chat.on_bot_join`**   [Skip link to [object Object]](https://docs.recall.ai/docs/sending-chat-messages\#send-a-message-when-the-bot-joins-chaton_bot_join)

| Parameter | Value | Description |
| --- | --- | --- |
| **`send_to`** | **Zoom:** `"host"` \| `"everyone"` \| `"everyone_except_host"`<br>**Meet:** `"everyone"`<br>**Teams:** `"everyone"` | Who the message will be sent to. |
| **`message`** | string | The message content to send. |
| **`pin`** | boolean | Whether to pin the message to the top of the chat. Pinned messages will be viewable for participants who join after the message was sent. Supported for Meet and Teams (Teams bots must be signed-in to pin messages) |

### **Send a message when a participant joins the call: `chat.on_participant_join`**   [Skip link to [object Object]](https://docs.recall.ai/docs/sending-chat-messages\#send-a-message-when-a-participant-joins-the-call-chaton_participant_join)

| Parameter | Value | Description |
| --- | --- | --- |
| **`exclude_host`** | boolean | Whether or not to trigger this message when the host joins. |
| **`message`** | string | The message content to send. |

## Using the Send Chat Messages endpoint   [Skip link to Using the Send Chat Messages endpoint](https://docs.recall.ai/docs/sending-chat-messages\#using-the-send-chat-messages-endpoint)

* * *

For more control over when bots send chat messages, Recall also provides an [endpoint](https://docs.recall.ai/reference/bot_send_chat_message_create) to send chat messages. This endpoint also allows you to pin messages.

Keep in mind that this endpoint has the same [platform limitations](https://docs.recall.ai/docs/sending-chat-messages#platform-limitations) outlined above.

### Send a chat message to a specific participant (Zoom only)   [Skip link to Send a chat message to a specific participant (Zoom only)](https://docs.recall.ai/docs/sending-chat-messages\#send-a-chat-message-to-a-specific-participant-zoom-only)

Using the [Send Chat Message](https://docs.recall.ai/reference/bot_send_chat_message_create) endpoint also has the benefit of being able to send chat messages as DM's to specific participants.

**Example: Send a message via DM to a specific Zoom participant**

1. First, you need the ID of the participant you'd like to send the DM to. For example, you can get this from the `meeting_participants` array in the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) response:



JSON





```rdmd-code lang-json theme-light

"meeting_participants": [\
         {\
           "id": 16778240,\
           "name": "John Doe",\
           "events": [\
             {\
               "code": "join",\
               "created_at": "2024-03-26T20:10:56.499605Z"\
             }\
           ],\
           "is_host": true,\
           "platform": "desktop",\
   				...\
         },\
         ...\
       ],

```

2. Now, to send a DM to John Doe, I can use his ID when calling [Send Chat Message](https://docs.recall.ai/reference/bot_send_chat_message_create):



cURL





```rdmd-code lang-curl theme-light

curl --request POST \
        --url https://us-east-1.recall.ai/api/v1/bot/3487f343-7ba6-4fe1-9462-08638b2ee51f/send_chat_message/ \
        --header 'Authorization: {TOKEN}' \
        --header 'accept: application/json' \
        --header 'content-type: application/json' \
        --data '
{
     "to": "16778240",
     "message": "Hello! I am a virtual meeting assistant that will be taking notes during this call."
}
'

```

3. The participant will then receive the message as a DM:

![](https://files.readme.io/5bfa387-CleanShot_2024-03-26_at_13.16.49.png)


## Sending formatted chat messages   [Skip link to Sending formatted chat messages](https://docs.recall.ai/docs/sending-chat-messages\#sending-formatted-chat-messages)

* * *

Teams supports sending hyperlinks in the chat using the following format: `<a href="https://example.com/">Example</a>`

Formatted chat messages are not supported for other meeting platforms at this time.

## Using chat messages for recording consent   [Skip link to Using chat messages for recording consent](https://docs.recall.ai/docs/sending-chat-messages\#using-chat-messages-for-recording-consent)

* * *

You may want to send a chat message at the start of a call to notify all participants that the call is being recorded. By default, people who join after this message is sent won't see it. You can choose to "pin" a message when you send it, which will make it visible for all participants for the entire meeting.

This is supported for both the automatic chat configuration in the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint and by using the [Send Chat Message](https://docs.recall.ai/reference/bot_send_chat_message_create) endpoint. This is available for both Meet and Teams. On Zoom, you can choose to [directly message individual participants](https://docs.recall.ai/docs/sending-chat-messages#send-a-chat-message-to-a-specific-participant-zoom-only) that the call is being recorded when they join.

Updated 13 days ago

* * *

Did this page help you?

Yes

No

Ask AI