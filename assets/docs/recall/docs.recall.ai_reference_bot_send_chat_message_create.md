---
url: "https://docs.recall.ai/reference/bot_send_chat_message_create"
title: "Send Chat Message"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  `to` parameter (Zoom only)
>
> In Zoom you can send a chat message as a DM to a specific participant by providing the `id` of the participant.
>
> You can get a participant's ID from the `id` field in the `meeting_participants` array when calling [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve).

**For more information, see [Chat Messages](https://docs.recall.ai/docs/chat-messages)**

id

uuid

required

A UUID string identifying this bot.

to

string

Defaults to everyone

The person or group that the message will be sent to. On non-Zoom platforms, "everyone" is currently the only supported option, meaning the message will be sent to everyone in the meeting.

message

string

required

length ≤ 4096

The message that will be sent.

pin

boolean

Defaults to false

truefalse

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{id}/send\_chat\_message/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/send_chat_message/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No