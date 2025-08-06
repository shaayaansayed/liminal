---
url: "https://docs.recall.ai/docs/calendar-v1-integration-guide"
title: "Integration Guide"
---

The calendar integration allows every unique user in your app to connect their Google/Microsoft calendars and have Recall bots join their meetings automatically.

Integrate Recall APIs directly into your Web/Mobile applications. Refer to our [demo app](https://recall-calendar-integration.pages.dev/) for an example integration ( [source code here](https://github.com/recallai/calendar-integration-demo/tree/master/v1-demo))

The following steps are needed for a unique user to connect their calendar and being auto-recording their meetings.

# Generate a calendar auth token   [Skip link to Generate a calendar auth token](https://docs.recall.ai/docs/calendar-v1-integration-guide\#generate-a-calendar-auth-token)

This token is used as authentication for all subsequent calls made to the calendar integration API endpoints. You can generate one using [this endpoint](https://docs.recall.ai/reference/calendar_authenticate_create). The token is stateless, has an expiry of 1 day and can be generated multiple times for a user. Few things to note are:

1. The `user_id` field should remain consistent for a specific user across multiple calls, failure to do so can result in duplicate calendar users and multiple bots joining the calls.
2. We recommend implementing a proxy endpoint on your servers for token generation (see e.g [here](https://github.com/recallai/calendar-integration-demo/tree/master/worker)). This ensures you do not expose your Recall API Key on the client.

# Initiate calendar connection   [Skip link to Initiate calendar connection](https://docs.recall.ai/docs/calendar-v1-integration-guide\#initiate-calendar-connection)

Setup OAuth clients on the calendar platforms(see [Google Calendar Setup](https://docs.recall.ai/reference/calendar-v1-google-calendar), [Microsoft Outlook Calendar Setup](https://docs.recall.ai/reference/calendar-v1-microsoft-outlook)\] for details) and redirect user to calendar connection URLs ( [code example here](https://github.com/recallai/calendar-integration-demo/blob/master/v1-demo/client/src/containers/Home/RecallCalendar/hooks/useRecallCalendar/index.ts)).

# Fetch Upcoming Meetings   [Skip link to Fetch Upcoming Meetings](https://docs.recall.ai/docs/calendar-v1-integration-guide\#fetch-upcoming-meetings)

Once a user's calendar is successfully connected. You can retrieve their upcoming meetings via [List Calendar Meetings](https://docs.recall.ai/reference/calendar_meetings_list) by passing the calendar auth token as `x-recallcalendarauthtoken` header in the request. The calendar integration automatically syncs updates to calendar events in near real-time, so every subsequent request to the list endpoint should give you the latest data.

For meetings that will be recorded by Recall, the meeting object would have `bot_id` attribute populated with the bot scheduled to join the meeting.

# Update recording preferences   [Skip link to Update recording preferences](https://docs.recall.ai/docs/calendar-v1-integration-guide\#update-recording-preferences)

Allow user to [Update Their Recording Preferences](https://docs.recall.ai/reference/calendar_user_update). See [Auto Recording Logic & Preferences](https://docs.recall.ai/reference/calendar-v1-recording-preferences) for more details

# Configuring Calendar Bots   [Skip link to Configuring Calendar Bots](https://docs.recall.ai/docs/calendar-v1-integration-guide\#configuring-calendar-bots)

> ## 📘  Updating your configuration
>
> To update your Calendar V1 bot configuration, reach out to our team in Slack and include the JSON you'd like to update the configuration to.

Bots scheduled via the calendar integration derive their configuration from a pre-populated preset. Bots will join 2 minutes before the scheduled start time of the meeting.

**All options available in [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint are supported here.**

Here are a few examples for reference:

_Settings transcription provider for calendar bots_

JSON

```rdmd-code lang-Text theme-light

{
  "recording_config": {
  	"transcript": {
    	"provider": {
      	"meeting_captions": {}
      }
    }
  },
}

```

_Enabling real time transcription for calendar bots_

JSON

```rdmd-code lang-Text theme-light

{
  "recording_config": {
  	"transcript": {
    	"provider": {
      	"meeting_captions": {}
      }
    },
    realtime_endpoints: [\
    	{\
      	"type": "webhook",\
        "events": ["transcript.data"],\
        "url": "..."\
      }\
    ]
  },
}

```

**Note: These apply to all calendar bots, incase you need more granular control over configuration(e.g per user/per event) please checkout Calendar V2 API**

> ## ❗️  Patching not supported
>
> Since Calendar V1 bots get their configuration from this preset as they join meetings, Patch requests to [Update Scheduled Bot](https://docs.recall.ai/reference/bot_partial_update) won't have an effect on the bot configuration.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI