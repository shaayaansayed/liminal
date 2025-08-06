---
url: "https://docs.recall.ai/docs/calendar-integration-faq"
title: "Calendar Integration FAQ"
---

# How far into the future are calendar events synced in the API?   [Skip link to How far into the future are calendar events synced in the API?](https://docs.recall.ai/docs/calendar-integration-faq\#how-far-into-the-future-are-calendar-events-synced-in-the-api)

4 weeks.

# How long does Recall store calendar data?   [Skip link to How long does Recall store calendar data?](https://docs.recall.ai/docs/calendar-integration-faq\#how-long-does-recall-store-calendar-data)

Recall will retain calendar data up to 60 days in the past for both Calendar V1 & V2 integrations. Calendar events past 60 days are automatically removed and not available via the API.

# How do I add a bot to a calendar event via email?   [Skip link to How do I add a bot to a calendar event via email?](https://docs.recall.ai/docs/calendar-integration-faq\#how-do-i-add-a-bot-to-a-calendar-event-via-email)

You may prefer a user flow where you can invite an email (eg. [notetaker@yourdomain.com](mailto:notetaker@yourdomain.com)) to any meeting, and the bot will join.

You can accomplish this with the Recall Calendar Integration by:

1. Creating an email on your end (e.g. [notetaker@yourdomain.com](mailto:notetaker@yourdomain.com))
2. Connecting that user to the [Recall calendar integration](https://docs.recall.ai/reference/calendar-integration)
3. Setting the calendar integration to automatically record every meeting on the calendar

This will assign a meeting bot to all events that your chosen email address is invited to.

# Does the calendar integration support team/shared calendars?   [Skip link to Does the calendar integration support team/shared calendars?](https://docs.recall.ai/docs/calendar-integration-faq\#does-the-calendar-integration-support-teamshared-calendars)

Currently only the primary calendar of connected users are supported.

# Are Microsoft Exchange On-premise Calendars supported?   [Skip link to Are Microsoft Exchange On-premise Calendars supported?](https://docs.recall.ai/docs/calendar-integration-faq\#are-microsoft-exchange-on-premise-calendars-supported)

Currently Microsoft Exchange On-premise calendars are not supported.

# Why do two Recall calendar events have different attendee information for the same underlying event?   [Skip link to Why do two Recall calendar events have different attendee information for the same underlying event?](https://docs.recall.ai/docs/calendar-integration-faq\#why-do-two-recall-calendar-events-have-different-attendee-information-for-the-same-underlying-event)

Data for the same event on different users' calendars can appear different because of [user-level event visibility settings](https://support.google.com/calendar/answer/34580?hl=en&co=GENIE.Platform%3DDesktop).

# Troubleshooting   [Skip link to Troubleshooting](https://docs.recall.ai/docs/calendar-integration-faq\#troubleshooting)

* * *

## `invalid_scope` error   [Skip link to [object Object]](https://docs.recall.ai/docs/calendar-integration-faq\#invalid_scope-error)

Even after setting up your OAuth client and successfully integrating calendars, you may see an `invalid_scope` error:

```rdmd-code lang- theme-light
"invalid_scope(detail: None of the supported calendar scopes(['https://www.googleapis.com/auth/calendar.events.readonly', 'https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar']) present in response(['https://www.googleapis.com/auth/userinfo.email', 'openid']).)"

```

This happens when the user is connecting their calendar for the first time, and doesn't select the checkbox to allow your app to view their calendar events.

![](https://files.readme.io/a0491cd-invalid_scope.png)

To resolve this, they should reconnect their calendar while ensuring to check this box.

Updated 27 days ago

* * *

Did this page help you?

Yes

No

Ask AI