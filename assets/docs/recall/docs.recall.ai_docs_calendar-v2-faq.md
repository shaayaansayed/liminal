---
url: "https://docs.recall.ai/docs/calendar-v2-faq"
title: "Calendar V2 FAQ"
---

# Grouping recurring calendar events   [Skip link to Grouping recurring calendar events](https://docs.recall.ai/docs/calendar-v2-faq\#grouping-recurring-calendar-events)

You may want to group all instances of a recurring event for tracking and applying recording preferences on these events.

If you're using the Calendar V2 integration, we recommend using these fields to group instances of a recurring events:

- `seriesMasterId` \- Microsoft Outlook
- `recurringEventId` \- Google Calendar

Since these are calendar platform-specific, you can find them in the `raw` attribute of the calendar event object.

# What if multiple bots from different apps using Recall try to join the same meeting?   [Skip link to What if multiple bots from different apps using Recall try to join the same meeting?](https://docs.recall.ai/docs/calendar-v2-faq\#what-if-multiple-bots-from-different-apps-using-recall-try-to-join-the-same-meeting)

Deduplication keys are scoped to a given Recall account. This means that multiple bots should have no trouble joining the same meeting, even if both companies are using the same deduplication key scheme.

# Why is the `platform_email` `null` when I create the calendar?   [Skip link to Why is the ](https://docs.recall.ai/docs/calendar-v2-faq\#why-is-the-platform_email-null-when-i-create-the-calendar)

The `​platform­_email​` may be ​null​ briefly when you create the calendar. This is because the calendar sync (which populates the `​platform­_email​`) happens asynchronously after the calendar is created.

If you need the email immediately, we'd recommend using the OAuth token to call the calendar platform (Google or Microsoft) APIs directly to retrieve the user email.

# Why did a calendar fail to connect with an `invalid_scope` error?   [Skip link to Why did a calendar fail to connect with an ](https://docs.recall.ai/docs/calendar-v2-faq\#why-did-a-calendar-fail-to-connect-with-an-invalid_scope-error)

Calendars can fail to connect due to `invalid_scope` for one of two reasons:

1. The OAuth client is setup incorrectly (e.g. missing necessary scopes in the OAuth client setup)
2. The end user did not grant the necessary permissions when connecting their account. This can happen when they forget to click a checkbox during the OAuth flow.

![If a user doesn't click the highlighted checkbox, this can result in an `invalid_scope` error on their calendar.](https://files.readme.io/ecdc43a-calendar-integraiton-checkbox.png)

If a user doesn't click the highlighted checkbox, this can result in an `invalid_scope` error on their calendar.

To resolve this, the user should reconnect their calendar while ensuring to check the checkbox.

# AADSTS7000215 Error   [Skip link to AADSTS7000215 Error](https://docs.recall.ai/docs/calendar-v2-faq\#aadsts7000215-error)

This indicates something is wrong with your OAuth client secret, for instance:

- **The secret expired**: In this case, you should [generate a new secret](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/create-or-update-client-ids-and-secrets#update-the-client-secret-associated-with-your-client-id), and [update](https://docs.recall.ai/reference/calendars_partial_update) any outlook calendars with the new secret value.
- **You've regenerated the secret, and haven't updated calendars in Recall:** In this case, you should [update](https://docs.recall.ai/reference/calendars_partial_update) any calendars with the new secret value.

_In both scenarios, updating the calendars' `client_secret` will kick off a reconnection._

# Why did the Calendar ID Associated with an Event ID Change?   [Skip link to Why did the Calendar ID Associated with an Event ID Change?](https://docs.recall.ai/docs/calendar-v2-faq\#why-did-the-calendar-id-associated-with-an-event-id-change)

Calendar events can have their calendar IDs changed on rare occasions due to a process called [event ownership transfer](https://support.google.com/calendar/answer/78739?hl=en&co=GENIE.Platform%3DDesktop). This happens when the ownership of an event is moved from one calendar to another, resulting in the same event ID being linked to a new calendar ID.

Such changes can occur unexpectedly, especially when events are managed by users within the same organization. If your system depends on a stable calendar ID, you may need to account for this scenario in your workflows.

# Why is the `onlineMeeting.joinUrl` populated on an event, but the `meeting_url` is not?   [Skip link to Why is the ](https://docs.recall.ai/docs/calendar-v2-faq\#why-is-the-onlinemeetingjoinurl-populated-on-an-event-but-the-meeting_url-is-not)

This can happen when the meeting URL is a wrapped link or is a link to a meeting on an unsupported platform.

# My Microsoft OAuth client secret is expiring. How do I migrate to a new secret?   [Skip link to My Microsoft OAuth client secret is expiring. How do I migrate to a new secret?](https://docs.recall.ai/docs/calendar-v2-faq\#my-microsoft-oauth-client-secret-is-expiring-how-do-i-migrate-to-a-new-secret)

Refresh tokens from Microsoft OAuth are not tied to specific client secrets.

This means that you can safely [update](https://docs.recall.ai/reference/calendars_partial_update) any calendars with the new secret, and Recall will automatically start using the new secret. End users do not need to reconnect.

In other words, you just need to:

- [Generate](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-renew-expiring-application-credential?tabs=microsoft-entra-admin-center#action-plan) a new OAuth secret
- [Update](https://docs.recall.ai/reference/calendars_partial_update) any calendars with the new `oauth_client_secret` value

Recall will automatically handle the rest, no end user action required.

# Why is the attendees field missing on the calendar event?   [Skip link to Why is the attendees field missing on the calendar event?](https://docs.recall.ai/docs/calendar-v2-faq\#why-is-the-attendees-field-missing-on-the-calendar-event)

This happens when there are no attendees on the calendar event so the meeting platform omits it

# Why are there missing attendees on the calendar event?   [Skip link to Why are there missing attendees on the calendar event?](https://docs.recall.ai/docs/calendar-v2-faq\#why-are-there-missing-attendees-on-the-calendar-event)

This happens when the host unchecks the `Guest Permissions` \> `See guest list` checkbox

![](https://files.readme.io/feebf9e92a3e774cf827e7bb982ea94c35b5eb76e63207c8370e4c66cd06e340-CleanShot_2025-05-19_at_10.35.412x.png)

# How to reconnect a disconnected calendar?   [Skip link to How to reconnect a disconnected calendar?](https://docs.recall.ai/docs/calendar-v2-faq\#how-to-reconnect-a-disconnected-calendar)

To reconnect a disconnected calendar, you can call the [Update Calendar](https://docs.recall.ai/reference/calendars_partial_update) endpoint with an empty body. If the authorization is still valid, the calendar will reconnect

# What happens on calendar disconnection?   [Skip link to What happens on calendar disconnection?](https://docs.recall.ai/docs/calendar-v2-faq\#what-happens-on-calendar-disconnection)

When a calendar becomes disconnected, all bots for future events are unscheduled. The calendar events are still queryable as the calendar resource has not been deleted

Note that there is a difference between calendar disconnection and calendar deletion. When you delete a calendar, the calendar and calendar events resources are no longer queryable and all bots are unscheduled from future events

The difference between these two in how they occur is a calendar disconnection is usually done by the user and a calendar deletion is done by you via the Delete Calendar api

# Why did my calendar fail to connect with error AADSTS900144?   [Skip link to Why did my calendar fail to connect with error AADSTS900144?](https://docs.recall.ai/docs/calendar-v2-faq\#why-did-my-calendar-fail-to-connect-with-error-aadsts900144)

If your calendar fails to connect with this error, it's very likely that your OAuth URL was constructed incorrectly. Check two things:

1. Make sure that your OAuth URL starts with `https://login.microsoftonline.com/common/oauth2/v2.0/authorize?...`
2. You should also make sure that the spaces in the `scope` query parameter are URL encoded. For example: `scope=offline_access%20User.Read%20Calendars.Read%20OnlineMeetings.Read`

Updated 6 days ago

* * *

Did this page help you?

Yes

No

Ask AI