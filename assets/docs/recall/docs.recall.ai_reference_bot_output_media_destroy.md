---
url: "https://docs.recall.ai/reference/bot_output_media_destroy"
title: "Output Media"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> By default, this api doesn't stop output media unless you specify one of the below params to `true`

id

uuid

required

A UUID string identifying this bot.

camera

boolean

Defaults to false

Stop outputting media on the bot camera

truefalse

screenshare

boolean

Defaults to false

Stop outputting media on the bot screenshare

truefalse

`` 204

No response body

Updated 24 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{id}/output\_media/

```

xxxxxxxxxx

1curl --request DELETE \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/output_media/ \

3     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here!

Updated 24 days ago

* * *

Did this page help you?

Yes

No