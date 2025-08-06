---
url: "https://docs.recall.ai/reference/recording_list"
title: "List Recordings"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

# Custom Metadata Filtering   [Skip link to Custom Metadata Filtering](https://docs.recall.ai/reference/recording_list\#custom-metadata-filtering)

To filter recordings by metadata, add query params in the form `metadata__KEY=VALUE`. When a metadata key / value pair is used only recordings with all of the key / value pairs as metadata will be returned.

bot\_id

uuid

created\_at\_after

date-time

created\_at\_before

date-time

cursor

string

The pagination cursor value.

desktop\_sdk\_upload\_id

uuid

status\_code

string \| null

- `processing` \- Processing
- `paused` \- Paused
- `done` \- Done
- `failed` \- Failed

donefailedpausedprocessing

# `` 200

Updated 2 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/recording/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/recording/ \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 2 days ago

* * *

Did this page help you?

Yes

No