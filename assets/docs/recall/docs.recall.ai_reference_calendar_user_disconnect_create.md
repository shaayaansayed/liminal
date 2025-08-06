---
url: "https://docs.recall.ai/reference/calendar_user_disconnect_create"
title: "Disconnect Calendar Platform"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> For more information, see [Calendar V1](https://docs.recall.ai/docs/calendar-v1-1).

You can get the `recallcalendarauthtoken` by calling the [Get Calendar Auth Token](https://docs.recall.ai/reference/calendar_authenticate_create) api

platform

string

required

- `google` \- Google
- `microsoft` \- Microsoft

googlemicrosoft

# `` 200

Updated 3 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/calendar/user/disconnect/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/calendar/user/disconnect/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "platform": "google"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 days ago

* * *

Did this page help you?

Yes

No