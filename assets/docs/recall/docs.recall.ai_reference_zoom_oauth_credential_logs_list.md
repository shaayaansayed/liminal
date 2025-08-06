---
url: "https://docs.recall.ai/reference/zoom_oauth_credential_logs_list"
title: "List Zoom OAuth Credential Logs"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see:
>
> - [Recall-Managed OAuth](https://docs.recall.ai/docs/recall-managed-oauth#calling-the-recall-api)
> - [Customer Managed OAuth](https://docs.recall.ai/docs/customer-managed-oauth#registering-the-callback-url-in-the-recall-api)

created\_at\_after

date-time

created\_at\_before

date-time

credential

uuid

cursor

string

The pagination cursor value.

ordering

string

Which field to use when ordering the results.

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/zoom-oauth-credential-logs/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/zoom-oauth-credential-logs/ \

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