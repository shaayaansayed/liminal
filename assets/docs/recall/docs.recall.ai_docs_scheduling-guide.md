---
url: "https://docs.recall.ai/docs/scheduling-guide"
title: "Scheduling Guide"
---

Once you've [successfully created a calendar in Recall](https://docs.recall.ai/docs/calendar-v2-integration-guide#4-create-calendar), you can start scheduling bots to calendar events for the same using the below steps:

# 1\. Sync Events   [Skip link to 1. Sync Events](https://docs.recall.ai/docs/scheduling-guide\#1-sync-events)

Once a calendar is connected, you will start receiving [calendar sync events](https://docs.recall.ai/reference/calendar-v2-webhooks#calendar-sync-events) webhooks whenever an event is added/updated/removed for the calendar. For each web-hook, you should (re)fetch the calendar events via [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list). You can choose to do either a full sync or use the `last_updated_ts` field in the payload (pass as `updated_at__gte` query parameter) to do an incremental sync(recommended).

Use the `is_deleted` field on the calendar event object to know if the event has been removed from the calendar or not. Recall does not delete any calendar events, and the consumer is expected to filter out events on basis of `is_deleted` attribute when syncing/displaying them to the end user.

_Note that created/deleted/updated events returned by [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list) will only reflect events within 1 day prior and 28 days into the future. For more info on this, see [here](https://docs.recall.ai/docs/scheduling-guide#how-does-the-time-window-of-events-returned-from-recall-work) ._

# 2\. Figure out recording status of an event   [Skip link to 2. Figure out recording status of an event](https://docs.recall.ai/docs/scheduling-guide\#2-figure-out-recording-status-of-an-event)

After events have been synced, for each calendar event, you should decide whether it needs to be recorded. You can use the `raw` data of the calendar event in combination with your application's business logic(e.g recording preferences of a user) to decide the same. Some examples below for reference are

1. Record external events


Use the `raw` data to extract list of attendees and check those against the email of the connected calendar.
2. Record confirmed events


Use the `raw` data to extract the response of the connected calendar email
3. Record all recurring instances of an event


Store the `ical_uid` of the recurring instance as recording preference of the user. For each event compare the `ical_uid` with the stored value to decide recording status.

# 3\. Add/Remove bot from the event   [Skip link to 3. Add/Remove bot from the event](https://docs.recall.ai/docs/scheduling-guide\#3-addremove-bot-from-the-event)

Based on the recording status of the calendar event, you should send request to either [Add Bot](https://docs.recall.ai/reference/calendar_events_bot_create) or [Remove Bot](https://docs.recall.ai/reference/calendar_events_bot_destroy) endpoint. For the case where a bot is already scheduled for the event, but the event's time was updated, you should call the [Schedule Bot for Calendar Event](https://docs.recall.ai/reference/calendar_events_bot_create) api.

The response object will contain the updated calendar event. The `bots` field will contain reference to bots(if any) that are scheduled to join the calendar event along with relevant metadata ( `deduplication_key`, `start_time`, `meeting_url`).

1. [Add Bot](https://docs.recall.ai/reference/calendar_events_bot_create)
   - Use `deduplication_key` to share bots across multiple calendar events. More on this in de-duplicating bots section below.
   - Use `bot_config` to specify the configuration for the bot. Incase multiple requests are made for the same calendar event, the config supplied in most recent request will get applied to the bot. For each request, include complete `bot_config` required ( **this endpoint does not support partial updates**). This allows you to have custom bot configuration based on the calendar event.
2. [Remove Bot](https://docs.recall.ai/reference/calendar_events_bot_destroy)
   - Delete scheduled bot for this event. The bot will only get deleted if it is not shared by any other calendar event(as a result of de-duplication).

> ## 📘  Deleted events
>
> Bots are automatically removed when a calendar event is deleted.

# 4\. Deduplicating Bots: Custom Bot Deduplication Key   [Skip link to 4. Deduplicating Bots: Custom Bot Deduplication Key](https://docs.recall.ai/docs/scheduling-guide\#4-deduplicating-bots-custom-bot-deduplication-key)

Deduplication allows you to share a bot across multiple calendar events. This is useful in cases where multiple connected calendars have a shared event marked for recording and you want to avoid scheduling multiple bots(1 bot for each calendar).

The `deduplication_key`(\*required field) allows you to create this grouping on your end. Some common use cases with recommended value for `deduplication_key` are listed below

- **Deduplicate All** (Recommended)


In this case you can set the `deduplication_key` to be `{event.start_time}-{event.meeting_url}`. It will ensure only 1 bot is scheduled across all connected calendars(for your Recall account)
- **Deduplicate by event and attendee's email domain**


In this case you set `deduplication_key` to be `{event.start_time}-{event.meeting_url}-{calendar_email_domain}`. It will ensure 1 bot per unique company domain across all connected calendars(for your Recall account) is scheduled.
- **No Deduplication**


You can set the `deduplication_key` to be `{event.start_time}-{event.meeting_url}-{event.id}`. It will schedule 1 bot per connected calendar for a shared event.

**Important**:

- The logic for generating the `deduplication_key` should remain consistent for all events. Failure to do so can result in unexpected scheduling behaviour. Incase you want to switch the de-duplication scheme from one to another, we recommend deleting all connected calendars and re-creating them.
- Deduplication keys only apply to future-scheduled bots. This means if you send a bot to a call, kick that bot, and schedule another bot for that event using the same deduplication key, this new bot will not be deduplicated.
- Deduplication keys are scoped to a given workspace. This means that if multiple workspaces use the same deduplication key for a calendar event, this will result in multiple bots joining.

# Scheduling Caveats   [Skip link to Scheduling Caveats](https://docs.recall.ai/docs/scheduling-guide\#scheduling-caveats)

While the above scheduling should work in most of the cases, you can run into unexpected values/responses from the API. Some of these are listed below for reference

## Perpetual Event   [Skip link to Perpetual Event](https://docs.recall.ai/docs/scheduling-guide\#perpetual-event)

In some cases a single calendar event is re-used by the user by moving it forward in the timeline after a specific occurrence. When recording such events, the `bots` field can contain multiple entries, 1 for each recorded occurrence of the event.

## Pre-poned Event   [Skip link to Pre-poned Event](https://docs.recall.ai/docs/scheduling-guide\#pre-poned-event)

A calendar event that is marked for recording in the future can get preponed to start in near future (<5m) from now. In such cases the response for [Add Bot](https://docs.recall.ai/reference/calendar_events_bot_create) endpoint can return with a `507`, this is due to not enough bots being available in the ad-hoc bot pool(the originally scheduled bot cannot be used in such cases as it's not ready to join the call in the updated time). We recommend, you retry the [Add Bot](https://docs.recall.ai/reference/calendar_events_bot_create) endpoint request in such cases.

## Updating Scheduled Bots   [Skip link to Updating Scheduled Bots](https://docs.recall.ai/docs/scheduling-guide\#updating-scheduled-bots)

If a bot is updated too close to the start of a calendar event, the bot may already be initialized and any changes made will not be applied.

We recommend making any changes at least 10 minutes before the start of the event to ensure any changes are applied accordingly.

## Handling 409s   [Skip link to Handling 409s](https://docs.recall.ai/docs/scheduling-guide\#handling-409s)

If multiple requests for adding/removing bot from a calendar event (with same deduplication\_key) are dispatched in parallel, you may receive `409` response status code for a sub-set of these. We recommend retrying these with a backoff on your end.

# Disconnecting/Deleting a calendar   [Skip link to Disconnecting/Deleting a calendar](https://docs.recall.ai/docs/scheduling-guide\#disconnectingdeleting-a-calendar)

When a user wants to disconnect their calendar, there are two ways they can do this:

1. Deleting their calendar from Recall.
2. Removing the OAuth connection from their Connected Apps on their Google/Microsoft account.

**Deleting their calendar from Recall (recommended)**

We **highly recommend** having a button or other trigger in your app that allows users to disconnect their calendar.

When they trigger this, you should call [Delete Calendar](https://docs.recall.ai/reference/calendars_destroy) using their calendar ID, which will immediately clean up bots scheduled to their calendar.

**Removing the OAuth connection from their Google/Microsoft account**

When a user removes your OAuth connection directly from their Google/Microsoft installed apps, bots will also be unscheduled from their calendar events.

**However**, Recall does not get notified when a user disconnects their calendar in this way, and so there can be a delay of up to a few hours before Recall is aware that they revoked their permission. This can lead to a delay in unscheduling any bots.

For this reason, we highly recommend allowing users to delete their calendars from your app directly, which will clean up any scheduled bots immediately.

# Handling rate limits   [Skip link to Handling rate limits](https://docs.recall.ai/docs/scheduling-guide\#handling-rate-limits)

Both the [Schedule Bot For Calendar Event](https://docs.recall.ai/reference/calendar_events_bot_create) and [Delete Bot From Calendar Event](https://docs.recall.ai/reference/calendar_events_bot_destroy) endpoints have their own respective rate limits (seen in the links above). Incase you are observing rate limit errors (returned as `Status Code: 429`) please review your integration to ensure

- Requests for events that are in the past are not being triggered (e.g triggering [Delete Bot From Calendar Event](https://docs.recall.ai/reference/calendar_events_bot_destroy) for events that have already ended)
- Request for events in the future are triggered in chronological order(this ensures most recent event schedules are updated first)

If you are experiencing rate limits issues even post these, please reach out to us for further assistance.

# FAQs   [Skip link to FAQs](https://docs.recall.ai/docs/scheduling-guide\#faqs)

* * *

## When calling Delete endpoint for a calendar, will bots scheduled for meetings associated with that calendar be automatically deleted ?   [Skip link to When calling Delete endpoint for a calendar, will bots scheduled for meetings associated with that calendar be automatically deleted ?](https://docs.recall.ai/docs/scheduling-guide\#when-calling-delete-endpoint-for-a-calendar-will-bots-scheduled-for-meetings-associated-with-that-calendar-be-automatically-deleted-)

The calendar delete operation ensures bots that are scheduled for all future meetings associated with the calendar will automatically get cleaned up. The API consumer does not need to explicitly unschedule bots before deleting the calendar

## The bot join time does not update if the calendar event’s time is changed. How should this be handled ?   [Skip link to The bot join time does not update if the calendar event’s time is changed. How should this be handled ?](https://docs.recall.ai/docs/scheduling-guide\#the-bot-join-time-does-not-update-if-the-calendar-events-time-is-changed-how-should-this-be-handled-)

You will receive [calendar sync events](https://docs.recall.ai/reference/calendar-v2-webhooks#calendar-sync-events) webhook whenever an event is updated for a calendar. This update can be change of one or more attributes of the calendar event e.g start time, attendees, meeting url etc.

For each of these webhook(s), you should re-fetch the calendar event and follow the below steps

1. Figure out if event should be recorded based on updated data. [https://recallai.readme.io/reference/scheduling-guide#2-figure-out-recording-status-of-an-event](https://recallai.readme.io/reference/scheduling-guide#2-figure-out-recording-status-of-an-event)
2. Trigger Add/Remove bot endpoint to update the bot schedule for the event. [https://recallai.readme.io/reference/scheduling-guide#3-addremove-bot-from-the-event](https://recallai.readme.io/reference/scheduling-guide#3-addremove-bot-from-the-event)

Recall does not automatically update the bot on changes to start time as this case will automatically be handled in the above implementation and ensures you add/remove bots using the latest event data on your end.

For e.g consider the below case

- Your application business logic requires not recording calls if attendees in an event do not belong to external domains.
- A connected calendar C1 has event E1 which has external attendees and has a bot scheduled to record it.
- Now E1 gets updated with a new start time and external attendees have been removed from it.
- Your business logic requires the bot to be unscheduled, however Recall cannot derive this on it's own looking at the raw calendar data, thus automatically re-scheduling the bot(by Recall) to new start time would not be desirable.

## The API only returns events from user's primary calendar. Does Recall support fetching events from other calendars the user has access to ?   [Skip link to The API only returns events from user's primary calendar. Does Recall support fetching events from other calendars the user has access to ?](https://docs.recall.ai/docs/scheduling-guide\#the-api-only-returns-events-from-users-primary-calendar-does-recall-support-fetching-events-from-other-calendars-the-user-has-access-to-)

The calendar integration only supports fetching events from the user's primary calendar at the moment. Please reach out to the team if you require support for accessing events on other calendars.

## How does the time window of events returned from Recall work?   [Skip link to How does the time window of events returned from Recall work?](https://docs.recall.ai/docs/scheduling-guide\#how-does-the-time-window-of-events-returned-from-recall-work)

Recall will fire a `calendar.sync_events` webhook whenever a change to the calendar's events is made.

However, the window in which calendar events are synced to Recall, and thus, will be displayed in any `updated_at__gte` queries to [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list), is as follows:

- **Future events:** 28 days

If events are scheduled outside of the 28 days, we will send a webhook as soon as the event enters the 28 day window. This ensures you don't miss any current or future events

For example, if a user makes a change to a calendar event 28 days in the future, this event will not appear when calling [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list). When the event is within 28 days from the current time, the event will appear in List Calendar Events and you will receive a webhook notification about the event

Since bots need not be scheduled outside of this window, Recall only stores and updates events within this sliding time window. If your app requires you to fetch events outside of this window, for example, to display events in your UI, then you can use the underlying OAuth token for the [calendar](https://docs.recall.ai/reference/calendars_retrieve) and fetch these directly from the meeting provider as needed.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI