---
url: "https://docs.recall.ai/reference/bot_output_audio_create"
title: "Output Audio"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information about outputting bot audio, see [Output Audio](https://docs.recall.ai/docs/output-audio-in-meetings).

id

uuid

required

A UUID string identifying this bot.

kind

string

required

- `mp3` \- mp3

mp3

b64\_data

string

required

length ≤ 1835008

Data encoded in Base64 format, using the standard alphabet (specified here: [https://datatracker.ietf.org/doc/html/rfc4648#section-4](https://datatracker.ietf.org/doc/html/rfc4648#section-4))

# `` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{id}/output\_audio/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/output_audio/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '{"kind":"mp3"}'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No