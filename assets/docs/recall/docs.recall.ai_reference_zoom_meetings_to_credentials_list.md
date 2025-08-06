---
url: "https://docs.recall.ai/reference/zoom_meetings_to_credentials_list"
title: "List Zoom Meeting to OAuth Credential Mappings"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘
>
> Recall uses mappings internally to determine which credential to use when automatically fetching join tokens for a meeting.
>
> Inspecting these mappings may be helpful when debugging bots that don't automatically record due to being unable to fetch join tokens.
>
> For more information, see [Testing Your Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging).

credential

uuid

cursor

string

The pagination cursor value.

meeting\_id

integer

ordering

string

Which field to use when ordering the results.

synced\_at\_after

date-time

synced\_at\_before

date-time

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/zoom-meetings-to-credentials/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v2/zoom-meetings-to-credentials/ \

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