---
url: "https://docs.recall.ai/reference/calendars_list"
title: "List Calendars"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).

created\_at\_\_gte

date-time

cursor

string

The pagination cursor value.

email

string

platform

string

- `google_calendar` \- Google Calendar
- `microsoft_outlook` \- Microsoft Outlook

google\_calendarmicrosoft\_outlook

status

string

- `connecting` \- Connecting
- `connected` \- Connected
- `disconnected` \- Disconnected

connectedconnectingdisconnected

# `` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/calendars/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/calendars/ \

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