---
url: "https://docs.recall.ai/docs/zoom-oauth-integration"
title: "Zoom OAuth Integration"
---

> ## 📘  Automatic Recording Privileges
>
> The Zoom OAuth integration is specifically for allowing bots to be able to record meetings without the host needing to manually grant recording access every meeting, as well as bypassing the waiting room.
>
> If you don't use this integration, Zoom bots will fall back to the default behavior of prompting the host for explicit recording permission every meeting.

To be compliant with Zoom's [requirements for meeting bots](https://docs.recall.ai/reference/zoom-new-bot-requirements), meeting bots need permission from the host to record. There are 2 ways to grant this permission:

1. The host can grant permission manually
2. The bot can be created with a [Join Token For Local Recording](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/meetingLocalRecordingJoinToken)

The Recall Zoom OAuth integration simplifies the process of implementing flow #2, automatically fetching Join Tokens for bots.

This is beneficial, because bots that have a "Join Token For Local Recording" are able to record meetings automatically when they join the call. This reduces user friction compared to the alternative flow, where the bot requests recording permission from the host, who has to click a dialog in order to grant the permission.

The other main benefits of this integration is that it enables bots to record when the host is not present.

# What does the Zoom OAuth Integration do?   [Skip link to What does the Zoom OAuth Integration do?](https://docs.recall.ai/docs/zoom-oauth-integration\#what-does-the-zoom-oauth-integration-do)

The integration does the following things:

1. Manages OAuth credentials, such as access and refresh tokens
2. Maintains a mapping between meeting IDs and Zoom OAuth credentials which are authorized to create a Join Token for that meeting ID
3. Automatically fetches a Join Token and provides it to the bot when sending the bot to a call. This means that when the bot joins the call, it will be able to start recording automatically instead of needing to ask the host for permission.

> ## ❗️  What this integration doesn't do
>
> The integration does **not** automatically send bots to calls.
>
> Bots will only be sent to calls if the bot is created with the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint or via the [Calendar Integration](https://docs.recall.ai/reference/calendar-integration).

# Flow Diagrams   [Skip link to Flow Diagrams](https://docs.recall.ai/docs/zoom-oauth-integration\#flow-diagrams)

![End user connects account, Recall receives webhooks from Zoo](https://files.readme.io/89f285c5da787f37460166e8992a676869fedf93e0cecae11463648a657a0423-CleanShot_2024-11-11_at_16.26.572x.png)

End user connects account. Recall begins receiving webhooks from Zoom.

![Bot is sent to end user's meeting, fetching a join token based on the ZoomMeetingToCredential mapping.](https://files.readme.io/41b4246e56b622dfcc170dcabb7ead42c14239453cda681185625c2bd49dc0e8-CleanShot_2024-11-11_at_16.24.072x.png)

Bot is sent to end user's meeting, fetching a join token based on the ZoomMeetingToCredential mapping.

Updated6 months ago

* * *

Did this page help you?

Yes

No

Ask AI