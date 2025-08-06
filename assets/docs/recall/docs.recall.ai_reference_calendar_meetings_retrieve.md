---
url: "https://docs.recall.ai/reference/calendar_meetings_retrieve"
title: "Retrieve Calendar Meeting"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V1](https://docs.recall.ai/docs/calendar-v1-1).

You can get the `recallcalendarauthtoken` by calling the [Get Calendar Auth Token](https://docs.recall.ai/reference/calendar_authenticate_create) api

id

uuid

required

A UUID string identifying this calendar meeting.

# `` 200

Updated 3 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/calendar/meetings/{id}/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/calendar/meetings/id/ \

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