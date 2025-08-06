---
url: "https://docs.recall.ai/reference/meeting_metadata_list"
title: "List Meeting Metadata"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

created\_at\_after

date-time

created\_at\_before

date-time

cursor

string

The pagination cursor value.

recording\_id

uuid

status\_code

string

- `processing` \- Processing
- `done` \- Done
- `failed` \- Failed

donefailedprocessing

# `` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/meeting\_metadata/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/meeting_metadata/ \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No