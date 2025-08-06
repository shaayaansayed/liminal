---
url: "https://docs.recall.ai/reference/google_logins_create"
title: "Create Google Login"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

**_Note: We recommend calling this endpoint using Postman, Insomnia, or a related tool, as cURL and the request sender in our docs are known to cause issues with PEM strings._**

> ## 📘
>
> For more information, see [Signed-In Google Meet Bots](https://docs.recall.ai/docs/google-meet-login-getting-started)

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

# `` 201

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/google-logins/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/google-logins/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201

Updated 3 months ago

* * *

Did this page help you?

Yes

No