---
url: "https://docs.recall.ai/reference/bot_screenshots_retrieve"
title: "Retrieve Bot Screenshot"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  Screenshots do not include participant video
>
> Bot screenshots are primarily a debugging tool, and aren't meant to be used for user-facing features.
>
> Because of this, screenshots do not include participant video.
>
> [More info](https://recallai.readme.io/docs/debugging-bots#bot-screenshots)

id

uuid

required

A UUID string identifying this bot screenshot.

bot\_id

uuid

required

The ID of the bot for which to retrieve the screenshot

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{bot\_id}/screenshots/{id}/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/bot/bot_id/screenshots/id/ \

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