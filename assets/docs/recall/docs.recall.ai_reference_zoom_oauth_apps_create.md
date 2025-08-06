---
url: "https://docs.recall.ai/reference/zoom_oauth_apps_create"
title: "Create Zoom OAuth App"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-oauth-integration)

kind

string

required

- `user_level` \- User Level
- `account_level` \- Account Level

user\_levelaccount\_level

client\_id

string

required

length ≤ 200

client\_secret

string

required

length ≤ 200

webhook\_secret

string

required

length ≤ 200

# `` 201

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/zoom-oauth-apps/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/zoom-oauth-apps/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "kind": "user_level"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201

Updated 3 months ago

* * *

Did this page help you?

Yes

No