---
url: "https://docs.recall.ai/reference/bot_screenshots_list"
title: "List Bot Screenshots"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  Screenshots do not include participant video
>
> Bot screenshots are primarily a debugging tool, and aren't meant to be used for user-facing features.
>
> Because of this, screenshots do not include participant video.
>
> [More info](https://recallai.readme.io/docs/debugging-bots#bot-screenshots)

bot\_id

uuid

required

The ID of the bot for which to retrieve the screenshots

action

string

Navigation direction ('prev' for previous page)

continuation\_token

string

Token for fetching the next page of results

meta

string

Encoded metadata for pagination state

recorded\_at\_after

date-time

Filter screenshots recorded after this datetime

recorded\_at\_before

date-time

Filter screenshots recorded before this datetime

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{bot\_id}/screenshots/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/bot/bot_id/screenshots/ \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No