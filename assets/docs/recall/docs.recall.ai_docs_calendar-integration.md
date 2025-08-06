---
url: "https://docs.recall.ai/docs/calendar-integration"
title: "Getting Started"
---

Recall supports integrating directly with your user's calendar to simplify sending bots and syncing them with calendar events. These integrations provide a simple way to take care of event updates, bot deduplication, and other complexities that come with integrating bots with calendars.

There are two methods to integrate bots with users' calendars:

1. [Calendar V1](https://docs.recall.ai/docs/calendar-v1-1)
2. [Calendar V2](https://docs.recall.ai/docs/v2)

Both integrations support Google Calendar and Microsoft Outlook, but there are a few key differences you should consider before proceeding.

# Choosing an integration: Calendar V1 vs V2   [Skip link to Choosing an integration: Calendar V1 vs V2](https://docs.recall.ai/docs/calendar-integration\#choosing-an-integration-calendar-v1-vs-v2)

In general, we recommend the Calendar V2 integration due to the extra modularity and control it gives your platform over bot configuration. In addition to more granular control over bot configuration, the Calendar V2 integration has the benefit of full control over scheduling bots. This is particularly useful if you want to implement your own user-level recording settings in your app.

If you're certain that you don’t need granular user-level bot configuration and are happy with something pre-canned, the Calendar V1 integration can save you a bit of time.

## Choose Calendar V2 if:   [Skip link to Choose Calendar V2 if:](https://docs.recall.ai/docs/calendar-integration\#choose-calendar-v2-if)

- You want to make bots highly customizable or want to tailor the bot experience granularly for each user.
- You want full control and flexibility over which calendar events should be recorded (e.g. want to apply your own business logic).
- You want to receive webhooks when a calendar gets connected and when calendar events are updated.
- You don’t mind spending a bit of extra dev time for modularity/flexibility.

To get started with the Calendar V2 Integration, check out our guide [here](https://docs.recall.ai/reference/calendar-v2-integration-guide).

## Choose Calendar V1 if:   [Skip link to Choose Calendar V1 if:](https://docs.recall.ai/docs/calendar-integration\#choose-calendar-v1-if)

- You don’t need a ton of flexibility in terms of which calendar events you need to record.
- You don’t mind having limited control over bot configuration (which includes things like recording options, transcription providers, and what your bot displays in the calls).
- You’re willing to lose some customizability to save a bit of development time.

Check out our Calendar V1 integration guide [here](https://docs.recall.ai/reference/calendar-v1-integration-guide).

Updatedabout 1 year ago

* * *

Did this page help you?

Yes

No

Ask AI