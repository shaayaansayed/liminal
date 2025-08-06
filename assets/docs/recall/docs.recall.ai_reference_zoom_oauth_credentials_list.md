---
url: "https://docs.recall.ai/reference/zoom_oauth_credentials_list"
title: "List Zoom OAuth Credentials"
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

account\_id

string

created\_at\_after

date-time

created\_at\_before

date-time

cursor

string

The pagination cursor value.

meeting\_sync\_status

string

This field tracks the status of initial meeting sync on the credential. This operation is processed asynchronously when the credential is created or when the sync meetings endpoint is called.

- `not_started` \- Not Started
- `in_progress` \- In Progress
- `completed` \- Completed
- `failed` \- Failed

completedfailedin\_progressnot\_started

oauth\_app

uuid

ordering

string

Which field to use when ordering the results.

status

string

- `healthy` \- Healthy
- `unhealthy` \- Unhealthy

healthyunhealthy

user\_id

string

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/zoom-oauth-credentials/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/zoom-oauth-credentials/ \

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