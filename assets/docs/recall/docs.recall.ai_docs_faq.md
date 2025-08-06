---
url: "https://docs.recall.ai/docs/faq"
title: "Bots FAQ"
---

## What does the sub code `timeout_exceeded_only_bots_in_call` mean ?   [Skip link to What does the sub code ](https://docs.recall.ai/docs/faq\#what-does-the-sub-code-timeout_exceeded_only_bots_in_call-mean-)

Some meeting platforms (e.g Google Meet/Teams) do not/partially support ending the meeting for all participants in the call. In such cases, if there are multiple bots in the call (Recall and/or other services), the Recall bots will not shutdown automatically solely based off the `automatic_leave.everyone_left_timeout` value. This is because the timeout value is considered if a _Recall bot is the only remaining participant in the call_.

In order to mitigate such scenarios, Recall bots will periodically(every 1m) check the call for existence of only bot participants and automatically shut down if the call has only bot participants in it, thus emitting the `timeout_exceeded_only_bots_in_call` call ended code.

**How is a participant categorised as bot ?**

Currently we use the voice activity based heuristic and if a participant has not produced any voice activity for the entire duration of the call (i.e no active speaker events) they are categorised as a bot participant.

Additionally there is a **buffer period of 10m at the beginning of the call during which bot detection is turned off**. This is present to avoid any false positives and bot's shutting down earlier than expected. (For e.g participant's joining in late, meeting starting late).

We are exploring alternative heuristics for bot detection to improve this further.

## What do negative speaker timeline timestamps mean?   [Skip link to What do negative speaker timeline timestamps mean?](https://docs.recall.ai/docs/faq\#what-do-negative-speaker-timeline-timestamps-mean)

The timestamp is second offsets to the bot `in_call_recording` event. Negative timestamps mean the active speaker change was received before the bot started recording. The bot joins the call first and records after a brief delay, as it takes a moment for the audio and video streams to connect

## How should I keep track of bot-hours used by my customers?   [Skip link to How should I keep track of bot-hours used by my customers?](https://docs.recall.ai/docs/faq\#how-should-i-keep-track-of-bot-hours-used-by-my-customers)

If you're implementing a pricing model where your customers have a fixed number of recording hours, you'll want to keep track of how many hours each customer is using. There are a few steps to this:

1. When calling [Create Bot](https://docs.recall.ai/reference/bot_create), keep track of which user the returned bot ID belongs to
2. When the bot completes, you'll get a `done` bot status webhook, containing the bot ID
3. You can then call [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) with that bot ID, and inspect the `status_changes` field
4. You can calculate the total time the bot recorded for by calculating the difference between timestamps of the `joining_call` event and the `done` event.

## Why am I not getting transcription?   [Skip link to Why am I not getting transcription?](https://docs.recall.ai/docs/faq\#why-am-i-not-getting-transcription)

The bot does not do transcription by default -- you must enable real-time transcription when you create the bot, or you must request async transcription once the bot has completed recording.

If you want real-time transcription, you must specify `recording_config.transcript` when [Creating the Bot](https://docs.recall.ai/reference/bot_create).

## Is bot data encrypted?   [Skip link to Is bot data encrypted?](https://docs.recall.ai/docs/faq\#is-bot-data-encrypted)

Bot data is encrypted at rest in our database for additional security.

## Why do my bots show up later than the `join_at` time?   [Skip link to Why do my bots show up later than the ](https://docs.recall.ai/docs/faq\#why-do-my-bots-show-up-later-than-the-join_at-time)

Since booting up and navigating to a specific meeting takes time, you may notice that your bots don't arrive exactly at the `join_at` time when scheduling bots. This is expected.

If your use case requires bots to show up exactly at a specific time (e.g. the top of the hour), then we recommend accounting for this by setting the `join_at` to be 10-15 seconds earlier.

## How do I update a lot of bots at once?   [Skip link to How do I update a lot of bots at once?](https://docs.recall.ai/docs/faq\#how-do-i-update-a-lot-of-bots-at-once)

Currently we don't have a batch update endpoint, so the recommended approach is to update each bot ID using the [Update Scheduled Bot](https://docs.recall.ai/reference/bot_partial_update) endpoint (or the [Schedule Bot For Calendar Event](https://docs.recall.ai/reference/calendar_events_bot_create) endpoint if using the Calendar V2 integration).

Keep in mind that these endpoints are rate limited to 600 requests/min.

## How can I close a websocket connection with the bot?   [Skip link to How can I close a websocket connection with the bot?](https://docs.recall.ai/docs/faq\#how-can-i-close-a-websocket-connection-with-the-bot)

There isn't a way to close a websocket with a bot. You should return success instead to avoid unnecessary reconnections

# Consent   [Skip link to Consent](https://docs.recall.ai/docs/faq\#consent)

* * *

## How do I get explicit consent from participants?   [Skip link to How do I get explicit consent from participants?](https://docs.recall.ai/docs/faq\#how-do-i-get-explicit-consent-from-participants)

One common way to get explicit consent from participants is to send emails to participants prior to the meeting, notifying them that the meeting will be recorded. Here you can provide a link that participants can click to provide their consent or non-consent, which you can keep track of for GDPR.

Another way is to have a custom meeting link where it redirects participants to a landing page where it tells the participants they will be recorded, and to only enter if they consent to be recorded. It should also include instructions for the user to withdraw their consent.

For more information, check out #4 and #5 on [this post](https://www.recall.ai/post/5-ways-to-request-recording-consent-with-meeting-bots).

Updated 10 days ago

* * *

Did this page help you?

Yes

No

Ask AI