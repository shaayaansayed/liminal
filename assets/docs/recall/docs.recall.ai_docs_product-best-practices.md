---
url: "https://docs.recall.ai/docs/product-best-practices"
title: "Best Practices"
---

# 1\. Add a Zoom OAuth   [Skip link to 1. Add a Zoom OAuth](https://docs.recall.ai/docs/product-best-practices\#1-add-a-zoom-oauth)

Because of [Zoom's new bot requirements](https://docs.recall.ai/reference/zoom-new-bot-requirements), we highly recommend you have your users OAuth their Zoom account for the best user experience. The best way we've seen this be done is by having a "Connect your Zoom" button in your product onboarding.

![Shows an example onboarding flow where the user first selects which meeting platform they use, then the next screen is a button to connect their Zoom account, which finally leads to the Zoom OAuth screen.](https://files.readme.io/4058f0b-Zoom_Oauth_Flow.png)

An example onboarding flow where the user first selects which meeting platform they use, then the next screen is a button to connect their Zoom account, which finally leads to the Zoom OAuth screen.

# 2\. Retry the recording request if permission is not granted   [Skip link to 2. Retry the recording request if permission is not granted](https://docs.recall.ai/docs/product-best-practices\#2-retry-the-recording-request-if-permission-is-not-granted)

The recording permission request pop up is a screen many users haven't seen before, and the bot may be denied recording permission on the first ask because of this.

If the bot is denied recording permission, you will get notified via a webhook with the message `recording_permission_denied`.

If you receive this webhook, we recommend using the [Send Chat Message](https://docs.recall.ai/reference/bot_send_chat_message_create) endpoint to trigger a private message to the host to give some context on why the bot is asking for recording permission. Then, have the bot ask for recording permission again.

This can increase the chances of the bot being allowed recording permission, especially if the host of the meeting is not your user.

# 3\. Have the bot display an image that clearly explains what it is   [Skip link to 3. Have the bot display an image that clearly explains what it is](https://docs.recall.ai/docs/product-best-practices\#3-have-the-bot-display-an-image-that-clearly-explains-what-it-is)

To increase chances of the host allowing the bot recording permission, have the bot display an image that explains what it is. You can do this by providing an JPEG to `automatic_video_output` parameter in the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint.

![An example image the bot could display that explains what it is](https://files.readme.io/549dde6-Recording_bot_profile_picture.png)

An example image the bot could display that explains what it is

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI