---
url: "https://docs.recall.ai/reference/calendar_events_list"
title: "List Calendar Events"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).

## `raw` field   [Skip link to [object Object]](https://docs.recall.ai/reference/calendar_events_list\#raw-field)

Examples of the platform-specific `raw` field data can be found at [Calendar Event Platform Data](https://docs.recall.ai/reference/calendar-event-platform-data).

A maximum of 100 events are returned. If more events exist, the response will include a `next` string with the full URL and cursor to retrieve the next page of paginated results.

Example:

json

```rdmd-code lang-json theme-light

{
  "next": "https://us-east-1.recall.ai/api/v2/calendar-events/?cursor=cD0yMDI0LTAyLTIyKzE2JTNBMTUlM0EwMCUyQjAwJTNBMDA%3D",
  "previous": null,
  "results": [...], // 100 events
}

```

calendar\_id

uuid

cursor

string

The pagination cursor value.

ical\_uid

string

Filter results by ical\_uid. (Case sensitive prefix match will be performed.)

is\_deleted

boolean

truefalse

start\_time

date-time

start\_time\_\_gte

date-time

start\_time\_\_lte

date-time

updated\_at\_\_gte

date-time

# `` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/calendar-events/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/calendar-events/ \

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