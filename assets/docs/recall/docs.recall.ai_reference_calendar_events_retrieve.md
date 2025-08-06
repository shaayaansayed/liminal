---
url: "https://docs.recall.ai/reference/calendar_events_retrieve"
title: "Retrieve Calendar Event"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).

## `raw` field   [Skip link to [object Object]](https://docs.recall.ai/reference/calendar_events_retrieve\#raw-field)

Examples of the platform-specific `raw` field data can be found at [Calendar Event Platform Data](https://docs.recall.ai/reference/calendar-event-platform-data).

id

uuid

required

A UUID string identifying this calendar event.

# `` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/calendar-events/{id}/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/calendar-events/id/ \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No