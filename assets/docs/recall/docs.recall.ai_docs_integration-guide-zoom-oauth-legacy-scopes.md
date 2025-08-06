---
url: "https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes"
title: "Zoom OAuth Setup: Legacy Scopes"
---

> ## 📘  Legacy scopes
>
> This guide is only for Zoom apps using Zoom's Legacy scopes.
>
> For Zoom apps created after March 21, 2024, see [Zoom OAuth Setup: Granular Scopes](https://docs.recall.ai/docs/integration-guide-zoom-oauth).

## Requesting the Required Scopes   [Skip link to Requesting the Required Scopes](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes\#requesting-the-required-scopes)

You'll need to request a few scopes on your OAuth app in order to use this integration.

If you already have an existing OAuth app and you're already having your users grant OAuth permission on Zoom, you can request the scopes on that app.

Otherwise, if you've [created Zoom SDK credentials to authenticate the bot](https://docs.recall.ai/reference/zoom-sdk-app-submission-guide), you can request the scopes on that app. You don't need to create a separate OAuth app, as the SDK app can also provide OAuth functionality.

Select the following scopes

1. From **Meeting** : `meeting:read`( _required to sync meetings_) and `meeting_token:read:local_recording`( _required to generate local recording token_)
2. From **User**: `user:read`( _required for retrieving user's PMI_) and `user_zak:read`

![](https://files.readme.io/650a30e-Screenshot_2023-12-18_at_12.00.11_PM.png)

![](https://files.readme.io/1f6625a-image.png)

![](https://files.readme.io/0194a63-Screenshot_2023-12-18_at_12.01.35_PM.png)

> ## 📘  PMI's and the `user:read` scope
>
> To make it obvious to the Zoom reviewer why this scope is needed, it's recommended to add a note to your application explaining this. We recommend the following:
>
> _Our application uses the OAuth integration to provide a seamless recording experience for users. Since personal meeting ID's are commonly used to host meetings by our users, and we'd like to provide the benefits of OAuth permissions for all of their meetings (including meetings hosted using their PMI), our application need this scope to fetch users' personal meeting IDs so we can provide OAuth tokens accordingly. Without the View User scope, we can't provide these tokens for Personal Meeting ID's, which would prevent our users from leveraging OAuth functionality for these meetings._

## Registering your OAuth App Credentials with Recall   [Skip link to Registering your OAuth App Credentials with Recall](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes\#registering-your-oauth-app-credentials-with-recall)

![](https://files.readme.io/21c1b63-image.png)

Once your app is created, click the "App Credentials" sidebar tab and note down the **Client ID** and **Client Secret**.

![](https://files.readme.io/ace639d-image.png)

Next, click the "Feature" sidebar tab, and take note of the **Secret Token** value ( `ZOOM_APP_SECRET_TOKEN`).

You'll provide this in the `webhook_secret` parameter in the next step.

### Create the Zoom OAuth App in Recall   [Skip link to Create the Zoom OAuth App in Recall](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes\#create-the-zoom-oauth-app-in-recall)

The next step is to create your Zoom OAuth App in Recall by calling the [Create Zoom OAuth App](https://docs.recall.ai/reference/zoom_oauth_apps_create) endpoint.

> ## ⚠️  Keep the returned ID!
>
> Store the `id` returned in the response somewhere easily accessible - you'll need this later.
>
> This is your **Recall Zoom OAuth App ID**.

Shell

```rdmd-code lang-shell theme-light

$ curl -X POST https://api.recall.ai/api/v2/zoom-oauth-apps/
	-H 'Authorization: Token YOUR-RECALL-API-KEY'
 	-H 'Content-Type: application/json'
  -d '{
    "kind": "user_level",
    "client_id": {ZOOM_APP_CLIENT_ID},
    "client_secret": {ZOOM_APP_CLIENT_SECRET},
    "webhook_secret": {ZOOM_APP_SECRET_TOKEN}
  }'


  // 201 Response example
  {
  	"id":"32721c6e-3acf-4511-851c-55772cfb34b7", // SAVE THIS FOR LATER!
    "kind":"user_level",
    "created_at":"2023-08-03T03:48:58.187545Z"
    ...
   }

```

## Configuring Webhooks   [Skip link to Configuring Webhooks](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes\#configuring-webhooks)

In order to automatically fetch tokens for a user's Zoom meetings, Recall needs a way to stay in sync with Zoom as new meetings are created.

To do this, we have to configure our Zoom app to send webhooks to a Recall endpoint - a webhook endpoint specific to the Zoom OAuth app you just created in the last step.

> ## ℹ️  Important: Zoom OAuth integration and bot behavior
>
> Configuring webhooks does **not** cause bots to automatically join Zoom meetings. It simply gives Recall the _ability_ to automatically fetch join tokens for any bots that you choose to send to these meetings.
>
> To actually create a bot and send it to a meeting, they still must be created through the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint or via the [Calendar Integration](https://docs.recall.ai/docs/calendar-integration).

The following are instructions to configure webhooks:

![](https://files.readme.io/7b3e1ff-marketplace.zoom.us_develop_apps_FkGS0K3jSkqv9sL0DmvT3A_feature.png)

**1\. Fill out the Event notification endpoint URLs**

Build your webhook URL using your **Recall Zoom OAuth App ID**:

`https://api.recall.ai/api/v2/zoom-oauth-apps/{RECALL_ZOOM_OAUTH_APP_ID}/webhook`

Do this for both development and production - these should be the same.

**If your server needs to receive these webhooks:**

- Enter your own server's webhook endpoint in these fields
- Forward every Zoom webhook received to the Recall endpoint constructed above
- You **must** include the `x-zm-request-timestamp` and `x-zm-signature` headers.
- You **must not** modify the webhook body in **any** way

**2\. Click the 'Validate' button**

This sends a test request to the URL to verify proper functioning.

If for some reason the validation fails:

- Check that your webhook URL is correct.
- Check that the `webhook_secret` you set while creating your Zoom OAuth App in Recall is correct.

**3\. Add the webhook events**

Click the "Add Events" button. A modal will show up. Select the following webhooks and then click "Done".

- In **Meeting** select the " **Meeting has been created**" event.

![](https://files.readme.io/2091de3-Screenshot_2023-12-18_at_12.41.33_PM.png)

- In **User** select the " **User's profile info has been updated** event. This is required to keep the personal meeting ID of the user in sync.

![](https://files.readme.io/4c084ab-Screenshot_2023-12-18_at_12.41.41_PM.png)

## Recall vs customer managed OAuth   [Skip link to Recall vs customer managed OAuth](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes\#recall-vs-customer-managed-oauth)

The next (and final) step is to implement the OAuth flow for your users in order to actually connect their Zoom accounts.

Once a user has gone through the flow, (has "OAuth-ed"), you can either manage access and refresh tokens on your end or have Recall manage these for you.

In general, we highly recommend using Recall-managed OAuth by default, **unless:**

- You already have an integration with the Zoom OAuth API.
- You need to call the Zoom API endpoints for other functionality in your app.

Updated 8 months ago

* * *

The OAuth Flow: Connect your customer's Zoom accounts.

- [Recall-Managed OAuth](https://docs.recall.ai/docs/recall-managed-oauth)
- [Customer Managed OAuth](https://docs.recall.ai/docs/customer-managed-oauth)

Did this page help you?

Yes

No

Ask AI