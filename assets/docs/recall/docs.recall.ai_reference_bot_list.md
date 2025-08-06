---
url: "https://docs.recall.ai/reference/bot_list"
title: "List Bots"
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

# Custom Metadata Filtering   [Skip link to Custom Metadata Filtering](https://docs.recall.ai/reference/bot_list\#custom-metadata-filtering)

To filter bots by metadata, add query params in the form `metadata__KEY=VALUE`. When a metadata key / value pair is used only bots with all of the key / value pairs as metadata will be returned.

join\_at\_after

date-time

join\_at\_before

date-time

meeting\_url

string

page

integer

A page number within the paginated result set.

platform

array of strings

- `zoom` \- Zoom
- `google_meet` \- Meet
- `goto_meeting` \- Goto
- `microsoft_teams` \- Teams
- `microsoft_teams_live` \- Teams Live
- `webex` \- Webex
- `chime_sdk` \- Chime Sdk
- `zoom_rtms` \- Zoom Rtms
- `google_meet_media_api` \- Google Meet Media Api
- `slack_authenticator` \- Slack Authenticator
- `slack_huddle_observer` \- Slack Huddle Observer

platform
ADD string

status

array of strings

- `ready` \- Ready
- `joining_call` \- Joining Call
- `in_waiting_room` \- In Waiting Room
- `in_call_not_recording` \- In Call Not Recording
- `recording_permission_allowed` \- Recording Permission Allowed
- `recording_permission_denied` \- Recording Permission Denied
- `in_call_recording` \- In Call Recording
- `recording_done` \- Recording Done
- `call_ended` \- Call Ended
- `done` \- Done
- `fatal` \- Fatal
- `media_expired` \- Media Expired
- `analysis_done` \- Analysis Done
- `analysis_failed` \- Analysis Failed

status
ADD string

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/

```

xxxxxxxxxx

1curl --request GET \

2     --url https://us-east-1.recall.ai/api/v1/bot/ \

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