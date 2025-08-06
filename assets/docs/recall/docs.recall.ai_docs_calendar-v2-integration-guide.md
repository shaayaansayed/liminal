---
url: "https://docs.recall.ai/docs/calendar-v2-integration-guide"
title: "Integration Guide"
---

# 1\. Initial setup   [Skip link to 1. Initial setup](https://docs.recall.ai/docs/calendar-v2-integration-guide\#1-initial-setup)

Create an API Key in the [Recall dashboard](https://api.recall.ai/dashboard/api-keys/). This will be used for API authentication.

# 2\. Setup OAuth Clients for Providers   [Skip link to 2. Setup OAuth Clients for Providers](https://docs.recall.ai/docs/calendar-v2-integration-guide\#2-setup-oauth-clients-for-providers)

Setup OAuth Providers for the calendar platforms you are planning to support.

- [Google Calendar](https://docs.recall.ai/reference/calendar-v2-google-calendar#setup-oauth-20-client)
- [Microsoft Outlook](https://docs.recall.ai/reference/calendar-v2-microsoft-outlook#setup-oauth-20-client)

Keep note of `CLIENT_ID`& `CLIENT_SECRET` values as they will be required later to connect calendar in Recall.

# 3\. Authorize User & Get Refresh Token   [Skip link to 3. Authorize User & Get Refresh Token](https://docs.recall.ai/docs/calendar-v2-integration-guide\#3-authorize-user--get-refresh-token)

At this point you should implement the OAuth 2.0 authorization code flow in your system.

1. Redirect the user to the authorization endpoint for a specific provider.
2. Receive a callback from the provider on successful connect.
3. Use the authorization code to retrieve a `refresh_token`. Refer to provider specific guides below

- [Google Calendar](https://docs.recall.ai/reference/calendar-v2-google-calendar#setup-oauth-20-client#implement-oauth-20-authorization-code-flow)
- [Microsoft Outlook](https://docs.recall.ai/reference/calendar-v2-microsoft-outlook#implement-oauth-20-authorization-code-flow)

# 4\. Create Calendar   [Skip link to 4. Create Calendar](https://docs.recall.ai/docs/calendar-v2-integration-guide\#4-create-calendar)

With the above data you can now proceed to [Create Calendar](https://docs.recall.ai/reference/calendars_create) in Recall. The following parameters will be needed

- `oauth_client_id`: (obtained in Step 2)
- `oauth_client_secret` (obtained in Step 2)
- `oauth_refresh_token`(obtained in Step 3)
- `platform` ( `google_calendar` or `microsoft_outlook`)

This will create a calendar in Recall which represents the **primary calendar** of the account that authorized the connection. Keep a hold of the `id` returned in the response. You can attach it to an entity that suits the business logic of your application.

> ## 📘  OAuth refresh tokens are long lived
>
> The refresh token you provide to Recall when creating a calendar is long-lived and allows us to manage refreshing a user's OAuth token for you automatically.
>
> A user's refresh token will only need to be updated if it's revoked by the user, which occurs in one of two cases:
>
> - The user manually revokes permissions (e.g. in Google or Microsoft settings)
> - The user changes their password and their user settings requires them to re-authenticate OAuth permissions
>
> When a user's refresh token is revoked, the calendar will become disconnected. In this case, the user should go through the OAuth flow and you should call [Update Calendar](https://docs.recall.ai/reference/calendars_partial_update) to update the refresh token accordingly.

# 5\. Process Web hooks   [Skip link to 5. Process Web hooks](https://docs.recall.ai/docs/calendar-v2-integration-guide\#5-process-web-hooks)

Once a calendar has been created you should start receiving web hooks related to updates for it via Svix. [Refer to this guide](https://docs.recall.ai/reference/calendar-v2-webhooks) on the type and how to handle each web hook.

# 6\. Fetch Calendar Events   [Skip link to 6. Fetch Calendar Events](https://docs.recall.ai/docs/calendar-v2-integration-guide\#6-fetch-calendar-events)

You can use the [List Calendar Events](https://docs.recall.ai/reference/calendar_events_list) to fetch the list of events for a specific calendar.

# 7\. Schedule bots to calendar events   [Skip link to 7. Schedule bots to calendar events](https://docs.recall.ai/docs/calendar-v2-integration-guide\#7-schedule-bots-to-calendar-events)

There are a couple of options here:

### Recall Managed Scheduling (Recommended)   [Skip link to Recall Managed Scheduling (Recommended)](https://docs.recall.ai/docs/calendar-v2-integration-guide\#recall-managed-scheduling-recommended)

Use Recall's scheduling endpoints to add/remove bots from calendar events with deduplication support. Please refer to the [Scheduling Guide](https://docs.recall.ai/docs/scheduling-guide) for more details.

### Self Managed Scheduling   [Skip link to Self Managed Scheduling](https://docs.recall.ai/docs/calendar-v2-integration-guide\#self-managed-scheduling)

With this option the API consumers can use the existing [Create Bot](https://docs.recall.ai/reference/bot_create) & [Delete Bot](https://docs.recall.ai/reference/bot_destroy) endpoints in combination with `meeting_url` & `start_time` values from a calendar event to add/remove bots to calendar events. This means the API consumer is responsible for managing the relationship b/w bots and calendar events completely on their end and handles cases such as de-duplication, event re-schedule/delete etc.

Updated 3 months ago

* * *

Did this page help you?

Yes

No

Ask AI