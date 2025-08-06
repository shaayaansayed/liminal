---
url: "https://docs.recall.ai/reference/google_login_groups_partial_update"
title: "Partial Update Google Login Group"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Signed-In Google Meet Bots](https://docs.recall.ai/docs/google-meet-login-getting-started)

id

uuid

required

A UUID string identifying this google login group.

name

string

length ≤ 2000

Name of the login group. It can used to filter out login groups when retrieving them via API.

login\_mode

string

- `always` \- Always
- `only_if_required` \- Only If Required

alwaysonly\_if\_required

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/google-login-groups/{id}/

```

xxxxxxxxxx

1curl --request PATCH \

2     --url https://us-east-1.recall.ai/api/v2/google-login-groups/id/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No