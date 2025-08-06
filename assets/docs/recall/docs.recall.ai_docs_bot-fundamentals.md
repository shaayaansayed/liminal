---
url: "https://docs.recall.ai/docs/bot-fundamentals"
title: "Bot Fundamentals"
---

# Scheduled vs. Ad Hoc Bots   [Skip link to Scheduled vs. Ad Hoc Bots](https://docs.recall.ai/docs/bot-fundamentals\#scheduled-vs-ad-hoc-bots)

There are two different ways of using bots:

1. Ad Hoc ("On-demand") bots - Bot joins call immediately. Very occasionally, the call to [Create Bot](https://docs.recall.ai/reference/bot_create) may return a [HTTP 507](https://recallai.readme.io/reference/errors#adhoc-bot-pool-errors). In this rare case, you can retry the call to Create Bot.
2. Scheduled bots - Bot is scheduled to join a call in the future, and is guaranteed to join.

**We highly recommend you use scheduled bots whenever possible.**

To use scheduled bots, you can either:

1. Specify the `join_at` parameter in the [Create Bot](https://recallai.readme.io/reference/bot_create) endpoint at least 10 minutes in advance
2. Use our [calendar integration](https://docs.recall.ai/docs/calendar-integration).

> ## 📘  Scheduling bots for the future using `join_at`
>
> The `join_at` parameter allows you to schedule bots for the future, and you may be wondering if there are limitations or best practices.
>
> In general, we recommend you to schedule a bot **as soon as you know about the meeting, and there is no limit how far into the future you can schedule bots.**

# Send Bots to Meetings   [Skip link to Send Bots to Meetings](https://docs.recall.ai/docs/bot-fundamentals\#send-bots-to-meetings)

There are a few different ways to send a bot to a meeting in Recall.

Depending on your app's requirements and use case, you'll likely want to use a combination of these options.

## Calling the Create Bot endpoint directly   [Skip link to Calling the Create Bot endpoint directly](https://docs.recall.ai/docs/bot-fundamentals\#calling-the-create-bot-endpoint-directly)

This is the most manual way to send a bot to a meeting, where you simply call the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint directly.

While it's the easiest to get started with and the most flexible, there may be a better way to create bots depending on your use case.

## Automatically schedule bots to calendar events   [Skip link to Automatically schedule bots to calendar events](https://docs.recall.ai/docs/bot-fundamentals\#automatically-schedule-bots-to-calendar-events)

The Recall calendar integration allow you to automatically schedule bots to send your users' calendar events, keeping scheduled bots in sync with any calendar changes.

For more information, check out our getting started guide [here](https://docs.recall.ai/docs/calendar-integration).

## Adding a bot email address to the meeting event   [Skip link to Adding a bot email address to the meeting event](https://docs.recall.ai/docs/bot-fundamentals\#adding-a-bot-email-address-to-the-meeting-event)

Another benefit of the Recall calendar integration is that it enables your users to add bots to meetings through inviting an email, just like you would any other participant.

To enable this flow, see [these instructions](https://docs.recall.ai/docs/calendar-integration-faq#how-do-i-add-a-bot-to-a-calendar-event-via-email).

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI