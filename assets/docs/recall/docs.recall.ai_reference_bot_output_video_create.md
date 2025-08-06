---
url: "https://docs.recall.ai/reference/bot_output_video_create"
title: "Output Video"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information on configuring bots to output an image, see [Output an Image](https://docs.recall.ai/docs/output-video-in-meetings).
>
> Outputting video and gifs is not supported through this endpoint. To output dynamic content, please see the [Output Media](https://docs.recall.ai/docs/stream-media) API.

id

uuid

required

A UUID string identifying this bot.

kind

string

required

- `jpeg` \- jpeg

jpeg

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

https://us-east-1.recall.ai/api/v1/bot/{id}/output\_video/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/output_video/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '{"kind":"jpeg"}'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No