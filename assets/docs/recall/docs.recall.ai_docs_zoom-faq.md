---
url: "https://docs.recall.ai/docs/zoom-faq"
title: "Zoom FAQ"
---

## What if Zoom returns an internal error?   [Skip link to What if Zoom returns an internal error?](https://docs.recall.ai/docs/zoom-faq\#what-if-zoom-returns-an-internal-error)

On rare occasions, your bot may fail to enter a call with a `zoom_internal_error` [sub code](https://docs.recall.ai/docs/sub-codes).

Unfortunately this means something went wrong on Zoom's end, and we have limited visibility into the underlying error. We do our best to handle these errors internally through retries but on rare occasions this error can cause a bot to fail.

If you're seeing this error recur for a certain situation or user, please let us know and we can raise the issue with Zoom.

## What happens if there is a password on the Zoom meeting?   [Skip link to What happens if there is a password on the Zoom meeting?](https://docs.recall.ai/docs/zoom-faq\#what-happens-if-there-is-a-password-on-the-zoom-meeting)

If there is a password on the meeting, it should be embedded in the meeting URL as a query parameter by default. For example, a meeting URL with an embedded password might look like this: [https://zoom.us/j/123?pwd=abc](https://zoom.us/j/123?pwd=abc). Everything after the `pwd=` in the URL is the password, which the bot will use to join the call.

If the password is not in the query parameter, the bot will not be able to join the call.

## Does the bot need to be let in every time?   [Skip link to Does the bot need to be let in every time?](https://docs.recall.ai/docs/zoom-faq\#does-the-bot-need-to-be-let-in-every-time)

The bot will go into the waiting room only if there is a waiting room enabled.

Think about the bot just like a normal participant. If there's a waiting room enabled, then it will go into the waiting room with other participants.

If there is no waiting room enabled, then it will skip the waiting room and join the meeting directly, just like other participants.

## Are Zoomgov URLs supported?   [Skip link to Are Zoomgov URLs supported?](https://docs.recall.ai/docs/zoom-faq\#are-zoomgov-urls-supported)

We currently don't have support for Zoomgov URLs, but if this is a requirement for your use case, please reach out to our team.

## Why isn't my bot sending chat messages?   [Skip link to Why isn't my bot sending chat messages?](https://docs.recall.ai/docs/zoom-faq\#why-isnt-my-bot-sending-chat-messages)

If the chat messages sent by your bot aren't showing up, it's likely a problem with your Zoom configuration. Please ensure that "Continuous Meeting Chat" is enabled on your Zoom account.

![](https://files.readme.io/743c501a76963f60eabad93a13bef499c43bac7a3c72028a8b11433222505581-CleanShot_2024-09-13_at_13.24.41.png)

You should also ensure that direct messages are enabled on your Zoom account.

![](https://files.readme.io/5de0f5ec6147da80ea02ca0ea3d019af07c11b09f9ff1234ae2e1796c217c3f9-CleanShot_2025-06-25_at_16.09.232x.png)

Updated 25 days ago

* * *

Did this page help you?

Yes

No

Ask AI