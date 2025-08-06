---
url: "https://docs.recall.ai/reference/calendar_meetings_refresh_create"
title: "Refresh Calendar Meetings"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> Recall keeps calendars in sync for you and you do not need to call this endpoint in order to get the most up-to-date version of users' calendars.
>
> For more information, see [Calendar V1](https://docs.recall.ai/docs/calendar-v1-faq#when-do-i-have-to-call-the-refresh-calendar-meetings-endpoint).

You can get the `recallcalendarauthtoken` by calling the [Get Calendar Auth Token](https://docs.recall.ai/reference/calendar_authenticate_create) api

# `` 200

Updated 3 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/calendar/meetings/refresh/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/calendar/meetings/refresh/ \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 days ago

* * *

Did this page help you?

Yes

No