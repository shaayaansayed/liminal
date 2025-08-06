---
url: "https://docs.recall.ai/reference/calendars_partial_update"
title: "Update Calendar"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).

id

uuid

required

A UUID string identifying this calendar.

oauth\_client\_id

string

length ≤ 2000

oauth\_client\_secret

string

length ≤ 2000

oauth\_refresh\_token

string

length ≤ 2000

platform

string

- `google_calendar` \- Google Calendar
- `microsoft_outlook` \- Microsoft Outlook

google\_calendarmicrosoft\_outlook

oauth\_email

string

length ≤ 2000

Show Deprecated

# `` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/calendars/{id}/

```

xxxxxxxxxx

1curl --request PATCH \

2     --url https://us-east-1.recall.ai/api/v2/calendars/id/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No