---
url: "https://docs.recall.ai/reference/dashboard_platforms_bots_screenshots_list"
title: "List Bot Screenshots"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

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

https://us-east-1.recall.ai/dashboard/platforms/bots/{bot\_id}/screenshots/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/dashboard/platforms/bots/bot_id/screenshots/ \

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