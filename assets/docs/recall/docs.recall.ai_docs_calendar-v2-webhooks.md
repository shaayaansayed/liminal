---
url: "https://docs.recall.ai/docs/calendar-v2-webhooks"
title: "Calendar V2 Webhooks"
---

The Calendar V2 API produces two types of webhooks, each scoped to a specific calendar and sent via Svix.

To configure a calendar V2 endpoint, you can follow [this setup guide](https://docs.recall.ai/docs/status-change-webhooks-setup-verification).

These webhooks are used to notify you about changes to calendars and their events, and you should use these to schedule bots and delete them according to your application logic.

# Events   [Skip link to Events](https://docs.recall.ai/docs/calendar-v2-webhooks\#events)

* * *

## Calendar Update   [Skip link to Calendar Update](https://docs.recall.ai/docs/calendar-v2-webhooks\#calendar-update)

This webhook is sent whenever the calendar's data changes (for instance, when `status` becomes `disconnected`).

JSON

```rdmd-code lang-Text theme-light

{
  "event": "calendar.update",
  "data": {
    "calendar_id": string,
  }
}

```

You should re-fetch the calendar via [Retrieve Calendar](https://docs.recall.ai/reference/calendars_retrieve) to get the latest state.

> ## 📘  Disconnects
>
> A calendar will become disconnected when:
>
> - You call the Delete Calendar endpoint
> - The refresh token of the user gets revoked, which can happen either:
>   - Explicitly removing your installed app
>   - The token becomes invalidated (for example, due to a user changing their password)
>
> _If your Google OAuth client is not approved yet, refresh tokens will [automatically expire after 7 days](https://developers.google.com/identity/protocols/oauth2#expiration)._

Note that you will not receive a `calendar.update` webhook event if you call the Delete Calendar endpoint as this action is initiated by you.

## Calendar Sync Events   [Skip link to Calendar Sync Events](https://docs.recall.ai/docs/calendar-v2-webhooks\#calendar-sync-events)

This webhook is sent whenever events on a calendar have been updated.

JSON

```rdmd-code lang-Text theme-light

{
  "event": "calendar.sync_events",
  "data": {
    "calendar_id": string,
    "last_updated_ts": string, // iso 8601 formatted datetime
  }
}

```

You should re-fetch the calendar events for this calendar via [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list). You can choose to do either a full sync or use the `last_updated_ts` field in the payload (pass as `updated_at__gte` query parameter) to do an incremental sync of events associated with the calendar on your end.

Use the `is_deleted` field on the calendar event object to know if the event has been removed from the calendar or not. (Note: Recall does not _delete_ any calendar events, the consumer is expected to filter out events on basis of `is_deleted` attribute when displaying them to the end user)

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI