---
url: "https://docs.recall.ai/reference/google_login_groups_update"
title: "Update Google Login Group"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

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

required

length ≤ 2000

Name of the login group. It can used to filter out login groups when retrieving them via API.

login\_mode

string

required

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

1curl --request PUT \

2     --url https://us-east-1.recall.ai/api/v2/google-login-groups/id/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "login_mode": "always"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No