---
url: "https://docs.recall.ai/reference/calendars_create"
title: "Create Calendar"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).

oauth\_client\_id

string

required

length ≤ 2000

oauth\_client\_secret

string

required

length ≤ 2000

oauth\_refresh\_token

string

required

length ≤ 2000

platform

string

required

- `google_calendar` \- Google Calendar
- `microsoft_outlook` \- Microsoft Outlook

google\_calendarmicrosoft\_outlook

oauth\_email

string

length ≤ 2000

Show Deprecated

# `` 201

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

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/calendars/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "platform": "google_calendar"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201

Updated 2 months ago

* * *

Did this page help you?

Yes

No