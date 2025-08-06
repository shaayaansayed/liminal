---
url: "https://docs.recall.ai/docs/calendar-v1-recording-preferences"
title: "Recording Preferences & Bot Deduplication"
---

# Recording Preferences   [Skip link to Recording Preferences](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#recording-preferences)

Calendar meetings do **not** get recorded by default.

The auto-recording behavior for synced calendar meetings can be configured based configured recording preferences, which can be updated via the [Update Recording Preferences](https://docs.recall.ai/reference/calendar_user_update) endpoint.

## Recording Prerequisites   [Skip link to Recording Prerequisites](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#recording-prerequisites)

Regardless of meeting preferences or manual recording overrides, a meeting must pass the following criteria in order to be recorded:

1. Must contain a valid meeting link.
2. Must have a both a start and end time (whole day events in are not supported).
3. Must not be cancelled and cannot have already ended.

## Manual Overrides   [Skip link to Manual Overrides](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#manual-overrides)

If a meeting passes [Recording Prerequisites](https://docs.recall.ai/docs/calendar-v1-recording-preferences#recording-prerequisites), the following conditions are applicable based on its `override_should_record` field value.

1. `null`: This is the default value. In this case, this field is ignored and [Recording Preferences](https://docs.recall.ai/docs/calendar-v1-recording-preferences#recording-preferences) apply.
2. `true`: The calendar meeting will be recorded, regardless of other preferences being applicable or not.
3. `false`: The calendar meeting will not be recorded, regardless of other preferences being applicable or not.

## Recording Preferences   [Skip link to Recording Preferences](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#recording-preferences-1)

A recording preference is applicable to a meeting only if:

1. Meeting passes [Recording Prerequisites](https://docs.recall.ai/docs/calendar-v1-recording-preferences#recording-prerequisites).
2. Meeting has `override_should_record` field value as `null`.
3. Preference value is `true`. ( _Note: Incase of `false` the preference is ignored rather than its negative being applicable_)

> ## 📘  Recording preferences behavior
>
> Only recording preference that are set to `true` will be evaluated. If all evaluated conditions are met, the meeting will be recorded.

Below is a list of supported preferences:

1. `record_non_host`: Meeting will be recorded only if the connected account is not the host of the meeting.
2. `record_external`: Meeting will be recorded only if it has at least 1 external attendee.
3. `record_internal`: Meeting will be recorded only if it has no external attendee.
4. `record_recurring`: Meeting will be recorded only if it is a recurring meeting.

An external attendee is defined as a participant having a different email domain than the email domain of the meeting host.

Additional preference filters( _Note: These settings act as additional filters on meetings that pass the above preference rules_):

1. `record_confirmed`: Meeting will only be recorded if the calendar account has "accepted" it.
2. `record_only_host`: Meeting will only be recorded if the calendar account is the host of the meeting.

## Common use cases and recording preference combinations   [Skip link to Common use cases and recording preference combinations](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#common-use-cases-and-recording-preference-combinations)

As the recording preferences build on top of each other, we recommend to avoid exposing these as direct options to your end users. Based on the use-cases your application needs to support, keep a map of preference object and apply it to the user.

We have listed few common use cases below along with preference object value. **For preference keys missing in the object, their value should be set to** `false`

**Record all meetings**

JSON

```rdmd-code lang-json theme-light

{
  record_non_host: false,
  record_recurring: false,
  record_external: true,
  record_internal: true,
  record_confirmed: false,
  record_only_host: false
}

```

**Record only internal meetings**

JSON

```rdmd-code lang-json theme-light

{
  record_non_host: false,
  record_recurring: false,
  record_external: false,
  record_internal: true,
  record_confirmed: false,
  record_only_host: false,
}

```

**Record only external meetings**

JSON

```rdmd-code lang-json theme-light

{
  record_non_host: false,
  record_recurring: false,
  record_external: true,
  record_internal: false,
  record_confirmed: false,
  record_only_host: false,
}

```

**Record only meetings where connected account is the host (both internal + external)**

JSON

```rdmd-code lang-json theme-light

{
  record_non_host: false,
  record_recurring: false,
  record_external: true,
  record_internal: true,
  record_confirmed: false,
  record_only_host: true,
}

```

**Record only meetings where connected account has accepted the invite (both internal + external)**

JSON

```rdmd-code lang-json theme-light

{
  record_non_host: false,
  record_recurring: false,
  record_external: true,
  record_internal: true,
  record_confirmed: true,
  record_only_host: false,
}

```

Incase of a missing use case, please reach out to us in the Slack to confirm the preference object combination.

## Customizing Name for Calendar Bots   [Skip link to Customizing Name for Calendar Bots](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#customizing-name-for-calendar-bots)

Calendar bot name can be configured for each user by updating the `bot_name` preference field. The changes can take few minutes to reflect for all the scheduled bots of the user.

* * *

## Bot Deduplication   [Skip link to Bot Deduplication](https://docs.recall.ai/docs/calendar-v1-recording-preferences\#bot-deduplication)

By default Recall will automatically de-duplicate bots(i.e send only 1 bot) for connected calendars scoped to a single Recall workspace. This would be better explained by example below:

Let’s say we have:

- Users U1 & U2 [u1@test.com](mailto:u1@test.com) & [u2@test.com](mailto:u2@test.com)
- Apps A1 & A2 using Recall’s calendar integration via their accounts [dev@a1.com](mailto:dev@a1.com) & [dev@a2.com](mailto:dev@a2.com) (both have de-duplication turned on their accounts)
- Both U1 & U2 connect their calendars in A1 & A2, and have a shared meeting M1 which needs to be auto-recorded.

How many bots should join the meeting M1 ?

1 - ❌ (This would mean both A1 & A2 have access to shared bot data which is incorrect)

2 - ✅ (One accessible to A1, One accessible to A2)

4 - ❌ (If de-duplication was turned off there would be 4 bots joining the call, U1A1, U1A2, U2A1, U2A2)

Incase a bot is de-duplicated across multiple meetings, the `calendar_meetings` array will contain reference to each of the calendar meeting.

**Opting out of de-deduplication**

If your application's business logic requires you to have 1 bot per connected calendar (i.e no deduplication). Please reach out to us and we can turn this off for your account.

**Custom de-deduplication**

The Calendar V1 APIs do not support supplying a custom de-deduplication logic. If you require this functionality, we recommend to integrate with [Calendar V2 APIs](https://docs.recall.ai/reference/calendar-v2-integration-guide).

**Deduplication Constraints**

- User Calendars must be using the same platform for deduplication to take place. One bot is sent for each calendar platform used by participants. That means if all meeting participants are using Google Calendars, then only 1 bot will be sent. If participants are using Google Calendar and Microsoft Outlook Calendars, then two bots will be sent.

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI