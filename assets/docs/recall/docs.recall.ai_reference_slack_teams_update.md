---
url: "https://docs.recall.ai/reference/slack_teams_update"
title: "Update Slack Team"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  Relevant Links
>
> [Slack Huddles Overview](https://docs.recall.ai/docs/slack-huddle-bots-overview)
>
> [Slack Bot Setup](https://docs.recall.ai/docs/slack-huddle-bots-integration-guide)

id

string

required

email\_address

string

required

The email address of the bot user. This is the email address that the customer will invite to their Slack workspace.

slack\_team\_domain

string

required

The domain of the Slack workspace that the bot user will be invited to. For instance "mycompany.slack.com".

bot\_name

string

required

The name of the bot user. This is the name that will be displayed in Slack.

profile\_photo\_base64\_jpg

string \| null

The profile photo of the bot user, encoded as a base64 string. This is the profile photo that will be displayed in Slack. This must be a 512x512px JPEG image.

auto\_join\_public\_huddles

boolean

required

Whether the bot user should automatically join huddles occuring in public channels.

truefalse

ask\_to\_join\_private\_huddles

boolean

required

Whether the bot user should ask to join huddles occuring in private channels.

truefalse

ask\_to\_join\_message

string

required

The message that the bot user will send when asking to join a private huddle.

filter\_huddles\_by\_user\_emails

array of strings \| null

A list of email addresses. If this is set, the bot user will only join huddles where one of the users is a participant of the huddle.

filter\_huddles\_by\_user\_emails
ADD string

huddle\_bot\_config

object

required

The configuration of the bot to join a huddle.

huddle\_bot\_config object

# `` 200

Updated 15 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/slack-teams/{id}/

```

xxxxxxxxxx

56

1curl --request PUT \

2     --url https://us-east-1.recall.ai/api/v2/slack-teams/id/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "auto_join_public_huddles": true,

8  "ask_to_join_private_huddles": true,

9  "huddle_bot_config": {

10    "recording_config": {

11      "retention": {

12        "type": "timed"

13      }

14    },

15    "output_media": {

16      "camera": {

17        "kind": "webpage"

18      },

19      "screenshare": {

20        "kind": "webpage"

21      }

22    },

23    "automatic_video_output": {

24      "in_call_recording": {

25        "kind": "jpeg"

26      },

27      "in_call_not_recording": {

28        "kind": "jpeg"

29      }

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 15 days ago

* * *

Did this page help you?

Yes

No