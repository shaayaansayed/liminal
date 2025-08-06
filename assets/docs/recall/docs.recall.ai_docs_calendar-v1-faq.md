---
url: "https://docs.recall.ai/docs/calendar-v1-faq"
title: "Calendar V1 FAQ"
---

## When do I have to call the Refresh Calendar Meetings endpoint?   [Skip link to When do I have to call the Refresh Calendar Meetings endpoint?](https://docs.recall.ai/docs/calendar-v1-faq\#when-do-i-have-to-call-the-refresh-calendar-meetings-endpoint)

When you update calendar preferences or a calendar event, you don't need to manually call the [Refresh Calendar Meetings](https://recallai.readme.io/reference/calendar_meetings_refresh_create) endpoint. Recall handles updating any relevant bots when changes are made to these.

## Linking bots to calendar user/meetings   [Skip link to Linking bots to calendar user/meetings](https://docs.recall.ai/docs/calendar-v1-faq\#linking-bots-to-calendar-usermeetings)

Bots scheduled via the calendar integration produce the status change events. On receiving these events, one common requirement is to link the bot back to a specific calendar meeting/user. Below are the steps for the same

1. Fetch bot data via [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) endpoint using `bot_id` from the event payload

2. The `calendar_meetings` array will contain all the meeting instances which were recorded by this specific bot. Use `calendar_user.external_id` to fetch [Get Calendar Auth Token](https://docs.recall.ai/reference/calendar_authenticate_create).

3. Use the auth token to fetch details for the meeting object via [Retrieve Calendar Meeting](https://docs.recall.ai/reference/calendar_meetings_retrieve) endpoint.


## How to detect if a user connected their calendar successfully or not ? OAuth callbacks are redirected to Recall's server.   [Skip link to How to detect if a user connected their calendar successfully or not ? OAuth callbacks are redirected to Recall's server.](https://docs.recall.ai/docs/calendar-v1-faq\#how-to-detect-if-a-user-connected-their-calendar-successfully-or-not--oauth-callbacks-are-redirected-to-recalls-server)

When [building the oAuth URL](https://docs.recall.ai/reference/calendar-v1-google-calendar), you can add `success_url` and/or `error_url` to the pass through `state` object. Recall will redirect the user to these depending on a successful/unsuccessful connection attempt. The query parameters attached to these are preserved allowing you to pass user context in these.

## What's the best way to allow users to disable a single calendar integration? [Delete Calendar User](https://docs.recall.ai/reference/calendar_user_destroy) disconnects all calendars.   [Skip link to What's the best way to allow users to disable a single calendar integration? ](https://docs.recall.ai/docs/calendar-v1-faq\#whats-the-best-way-to-allow-users-to-disable-a-single-calendar-integration-delete-calendar-user-disconnects-all-calendars)

To disconnect a specific calendar platform, you can use the [Disconnect Calendar Platform](https://docs.recall.ai/reference/calendar_user_disconnect_create) endpoint.

## What is `REACT_APP_AUTH_URL` in the [demo app source code](https://github.com/recallai/calendar-integration-demo/tree/master/v1-demo) ?   [Skip link to What is ](https://docs.recall.ai/docs/calendar-v1-faq\#what-is-react_app_auth_url-in-the-demo-app-source-code-)

The [Calendar Integration V1 APIs](https://docs.recall.ai/reference/calendar-v1-integration-guide) are designed to be directly integrated into the client. Due to this, there is need on your end to setup a server endpoint which token exchange (by calling the [https://recallai.readme.io/reference/calendar\_authenticate\_create](https://recallai.readme.io/reference/calendar_authenticate_create) endpoint on Recall's server). This needs to be a server endpoint to avoid exposing your Recall API Key on the client. The `REACT_APP_AUTH_URL` variable should contain the value for the endpoint. The demo code includes a [Cloudflare worker](https://github.com/recallai/calendar-integration-demo/tree/master/v1-demo/worker) to allow setting this up on your end without having to deploy a new endpoint on your backend.

## Can I connect two Google Calendars to the same user?   [Skip link to Can I connect two Google Calendars to the same user?](https://docs.recall.ai/docs/calendar-v1-faq\#can-i-connect-two-google-calendars-to-the-same-user)

The same calendar user cannot have multiple Google calendars (or multiple Microsoft calendars) connected to them. The latest connection will clear out bots and calendar data for any previous connections.

The same user **can** have one Google and one Microsoft calendar connected.

## What happens to scheduled bots when a user changes their recording preferences?   [Skip link to What happens to scheduled bots when a user changes their recording preferences?](https://docs.recall.ai/docs/calendar-v1-faq\#what-happens-to-scheduled-bots-when-a-user-changes-their-recording-preferences)

If a user updates their recording preferences to include fewer meetings, the calendar v1 integration will automatically remove scheduled bots from any upcoming meetings that no longer match the new preferences.

# Common Errors   [Skip link to Common Errors](https://docs.recall.ai/docs/calendar-v1-faq\#common-errors)

* * *

## **Refresh token missing from OAuth response**   [Skip link to [object Object]](https://docs.recall.ai/docs/calendar-v1-faq\#refresh-token-missing-from-oauth-response)

`Calendar connection failed! (reason: refresh_token missing from oAuth response)`

There are a couple of cases related to the setup of [Microsoft Outlook Calendar Setup](https://docs.recall.ai/reference/calendar-v1-microsoft-outlook) which can lead to the above error.

1. Incorrect/Misconfigured OAuth [credentials in dashboard](https://api.recall.ai/dashboard/platforms/microsoft) \- `client id, client secret` (verify steps 3, 5, 6).
2. `Supported Account Type` not set to **Accounts in any organizational directory (Any Azure AD directory - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)** (step 1). For this step, if you've already created an app registration without Multitenant support, we recommend to create a new registration from scratch as updating the existing one can still lead to above error.

Incase neither of the above help, please try connecting the same calendar account on [the demo app here](https://recall-calendar-integration.pages.dev/) and report the error to us in Slack.

## Invalid Recall calendar auth token supplied   [Skip link to Invalid Recall calendar auth token supplied](https://docs.recall.ai/docs/calendar-v1-faq\#invalid-recall-calendar-auth-token-supplied)

`Calendar connection failed! (Invalid ‘recall_calendar_auth_token’ supplied)`

This error occurs for one of two reasons:

- The auth token supplied is invalid: Either the token is invalid and couldn't be decoded
- The auth token has expired: Tokens have an expiry of 24h.

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI