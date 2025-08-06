---
url: "https://docs.recall.ai/reference/slack_teams_oauth_tokens_create"
title: "Create Slack User OAuth Token"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

slack\_team\_integration\_id

string

required

token

string

required

The OAuth token for the Slack user. Only a few characters are shown in responses.

# `` 201

Updated 12 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/slack-teams/{slack\_team\_integration\_id}/oauth-tokens/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/slack-teams/slack_team_integration_id/oauth-tokens/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201

Updated 12 days ago

* * *

Did this page help you?

Yes

No