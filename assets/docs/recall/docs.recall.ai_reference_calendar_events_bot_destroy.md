---
url: "https://docs.recall.ai/reference/calendar_events_bot_destroy"
title: "Schedule Bot For Calendar Event"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

For more information, see [Calendar V2 Scheduling Guide](https://docs.recall.ai/docs/scheduling-guide#3-addremove-bot-from-the-event).

> ## 🔄  This endpoint is idempotent
>
> A request method is considered _idempotent_ when executing multiple identical requests with that method yields the same outcome on the server as executing a single request of the same kind.
>
> This means that if the calendar event ID exists, both the first and any following requests will return `200` responses.

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

https://us-east-1.recall.ai/api/v2/calendar-events/{id}/bot/

```

xxxxxxxxxx

1curl --request DELETE \

2     --url https://us-east-1.recall.ai/api/v2/calendar-events/id/bot/ \

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