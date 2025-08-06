---
url: "https://docs.recall.ai/reference/realtime_endpoint_list"
title: "List Realtime Endpoints"
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

- `running` \- Running
- `done` \- Done
- `failed` \- Failed

donefailedrunning

type

string

- `rtmp` \- Rtmp
- `websocket` \- Websocket
- `webhook` \- Webhook
- `desktop_sdk_callback` \- Desktop Sdk Callback

desktop\_sdk\_callbackrtmpwebhookwebsocket

# `` 200

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/realtime\_endpoint/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/realtime_endpoint/ \

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