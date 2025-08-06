---
url: "https://docs.recall.ai/reference/bot_retrieve"
title: "Retrieve Bot"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 🚧  Meeting URL response shape
>
> Meeting URL's are currently improperly reflected in the API spec for **meeting URL's in responses**. For proper meeting URL shapes in API responses, please see [Meeting URL's](https://docs.recall.ai/docs/meeting-urls).
>
> `meeting_url`'s that are provided as a **parameter** to the API are reflected accurately in the API spec as strings.

**Relevant links:**

- [Meeting Metadata & Participants](https://docs.recall.ai/docs/meeting-metadata-and-participants)

id

uuid

required

A UUID string identifying this bot.

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{id}/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/ \

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