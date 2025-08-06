---
url: "https://docs.recall.ai/reference/zoom_oauth_credentials_create"
title: "Create Zoom OAuth Credential"
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

oauth\_app

uuid

required

authorization\_code

object

Data received from Zoom after the user has authorized the app. Applicable for **Recall Managed OAuth** flow.

authorization\_code object

access\_token\_callback\_url

string \| null

The url to retrieve access token from. Applicable for **Customer Managed OAuth** flow.

# `` 201

# `` 400

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

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/zoom-oauth-credentials/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201`` 400

Updated 3 months ago

* * *

Did this page help you?

Yes

No