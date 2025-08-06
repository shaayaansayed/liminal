---
url: "https://docs.recall.ai/reference/google_logins_update"
title: "Update Google Login"
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

A UUID string identifying this google login.

email

string

required

The email address of the google account to use for login.

is\_active

boolean

If the login should be used for round robin. (default: true)

truefalse

sso\_v2\_workspace\_domain

string

required

The primary domain name of your Google Workspace Account used for SSO.

sso\_v2\_private\_key

string

required

PEM-formatted private key used for signing SSO requests.

sso\_v2\_cert

string

required

PEM-formatted x509 certificate which is registered in your Google Workspace SSO Profile.

group\_id

uuid

required

The id of the login group this login belongs to.

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/google-logins/{id}/

```

xxxxxxxxxx

1curl --request PUT \

2     --url https://us-east-1.recall.ai/api/v2/google-logins/id/ \

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