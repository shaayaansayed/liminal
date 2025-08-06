---
url: "https://docs.recall.ai/docs/integration-guide-zoom-oauth"
title: "Zoom OAuth Setup"
---

> ## 📘  Granular scopes
>
> Zoom introduced new "granular" scopes in April 2024 to replace their Legacy scopes. Existing apps are unaffected, but any newly created apps will use these new granular scopes.
>
> For previously created apps using Legacy scopes, see [Zoom OAuth Setup](https://docs.recall.ai/docs/integration-guide-zoom-oauth-legacy-scopes).

# 1\. Zoom App Setup   [Skip link to 1. Zoom App Setup](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#1-zoom-app-setup)

* * *

## Create the App   [Skip link to Create the App](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#create-the-app)

Navigate to the [Zoom App marketplace](https://marketplace.zoom.us/) and select **Develop > Build App**

![Creating a new Zoom App](https://files.readme.io/d96c148-CleanShot_2024-04-23_at_13.35.56.png)

Creating a new Zoom App

Select **General App** in the dialog:

![](https://files.readme.io/cdbcaef-CleanShot_2024-07-08_at_14.41.032x.png)

Select how your users will manage your app:

- **User-managed:** Individual end users authenticate via OAuth
- **Account-managed:** Zoom account admins authenticate the app for their entire organization

![Select how the app is managed: User vs Admin-managed](https://files.readme.io/38f269d-CleanShot_2024-04-23_at_13.37.50.png)

Select how the app is managed: User vs Admin-managed

> ## 📘
>
> In general, if your app serves individual end users, you should default to User-managed. If your app is used by entire organizations, you should use admin-managed.

## Scopes   [Skip link to Scopes](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#scopes)

For the Zoom OAuth integration to work properly, we need to include a several OAuth scopes.

These are different for user-level and account-level apps - make sure to select the scopes accordingly.

### User-level (user-managed) scopes   [Skip link to User-level (user-managed) scopes](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#user-level-user-managed-scopes)

| Scope Name | Purpose |
| --- | --- |
| `meeting:read:local_recording_token` | This scope is used to retrieve the "Join Token For Local Recording", which is provided to the bot to allow it to automatically begin recording without prompting the host for permission. |
| `meeting:read:list_meetings` | This scope is used to enumerate all of a user's scheduled meetings, so that we can match meeting ID's to hosts. This enables us to generate a "Join Token for Local Recording" using the correct host credentials when a bot is sent to one of the meetings. |
| `meeting:read:meeting` | This scope is enabled automatically if `meeting:read:list_meetings` is enabled, and cannot be removed |
| `user:read:user` | This scope is used to read the user's Personal Meeting ID (PMI), so that a "Join Token for Local Recording" can be generated when a bot is sent to that meeting. |
| `user:read:zak` | This scope is enabled automatically if Meeting SDK functionality is enabled on your OAuth app, and cannot be removed |

![OAuth scopes for user-managed apps](https://files.readme.io/913d86e-CleanShot_2024-04-23_at_13.56.02.png)

OAuth scopes for user-managed apps

The `user:read:zak` scope is only required if you're using the same Zoom App to

provide Meeting SDK functionality to your Zoom bots.

For the scope description, we recommend the following:

> These scopes are used to give local recording permissions to meeting bots on behalf of the user. The user's ID as well as their meeting ID's (including their PMI) are stored in order to know which meetings to generate local recording join tokens for. All data is encrypted at rest.

### Account-level (admin-managed) scopes   [Skip link to Account-level (admin-managed) scopes](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#account-level-admin-managed-scopes)

| Scope Name | Purpose |
| --- | --- |
| `meeting:read:local_recording_token:admin` | This scope is used to retrieve the "Join Token For Local Recording", which is provided to the bot to allow it to automatically begin recording without prompting the host for permission. |
| `meeting:read:list_meetings:admin` | This scope is used to enumerate all users' scheduled meetings, so that a "Join Token for Local Recording" can be generated when a bot is sent to one of the meetings. |
| `user:read:list_users:admin` | This scope is used to read the users' Personal Meeting ID (PMI), so that a "Join Token for Local Recording" can be generated when a bot is sent to that meeting. |

![OAuth scopes for admin-managed apps](https://files.readme.io/e200dbb-CleanShot_2024-04-23_at_14.41.562x.png)

OAuth scopes for admin-managed apps

In the Scope Description, we recommend the following response:

> The local recording token scope is used to give meeting bots recording permission. The list users scope is used to retrieve all users for the Zoom account. The list meetings scope is used to get all meetings for a given user in the workspace. The users' meetings and account ID are stored in a database and are encrypted at rest.

> ## 📘  Note about data storage
>
> Zoom requires you to specify how data is stored when using additional scopes.
>
> Regardless of your app type, you should add the following to the description:
>
> > All data is encrypted using AES-256 encryption.

## Save your app details   [Skip link to Save your app details](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#save-your-app-details)

Once you've set up your Zoom app, you should save the following 3 pieces of information from your **Development** application:

- **Client ID**
- **Client Secret**
- **Secret Token**

Your client ID and client secret can be found under **Build your app > Basic Information** or in the Application Credentials card in the top left.

The Zoom App Secret Token can be found under **Build your app > Features > Access**

![The client ID and secret are necessary to call's Zoom's API to get a Local Recording Token.   The Secret Token is used to verify incoming webhooks from Zoom.](https://files.readme.io/2cb904f29bc48d1ab825c1d69ef83d4acde12848bb4202cf779d013af10a471e-CleanShot_2024-11-09_at_10.40.262x.png)

The client ID and secret are necessary to call's Zoom's API to get a Local Recording Token.

The Secret Token is used to verify incoming webhooks from Zoom.

> ## 📘
>
> We recommend storing these in a `.env` file for local development. This will make it simple to change these values to the corresponding production credentials when your Zoom app is approved.

# 2\. Create the OAuth App in Recall   [Skip link to 2. Create the OAuth App in Recall](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#2-create-the-oauth-app-in-recall)

* * *

### Create the app in the dashboard   [Skip link to Create the app in the dashboard](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#create-the-app-in-the-dashboard)

[Login to Recall](https://recall.ai/login) and go to the API Explorer dashboard.

On the Zoom OAuth page, select **Create App**.

Fill out the details, copied from the last step, and make sure to select User-managed or Admin-managed depending on your app type.

### Create the app via the API   [Skip link to Create the app via the API](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#create-the-app-via-the-api)

You can alternatively create the Zoom OAuth App in Recall by using the [Create Zoom OAuth App](https://docs.recall.ai/reference/zoom_oauth_apps_create) endpoint.

The body should include:

- `kind`: `user_level` or `account_level` depending on your app
- `client_id`: The client ID from the previous step
- `client_secret`: The client secret from the previous step
- `webhook_secret`: The secret token from the previous step

> ## 📘  Save the returned ID
>
> Store the id returned in the response somewhere easily accessible - you'll need this in the following steps.
>
> This is your **Recall Zoom OAuth App ID**.

# 3\. Configure webhooks   [Skip link to 3. Configure webhooks](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#3-configure-webhooks)

* * *

In order to automatically fetch tokens for a user's Zoom meetings, Recall needs a way to stay in sync with Zoom as new meetings are created.

To do this, we have to configure our Zoom app to send webhooks to a Recall endpoint - a webhook endpoint specific to the Zoom OAuth app you just created in the last step.

## Add events   [Skip link to Add events](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#add-events)

Navigate to the "Access" tab in the app dashboard. Toggle on "Event Subscription", click the "Add New Event Subscription" button, then the "Add Events" button, and select the following events:

**Meeting > Meeting has been created**

![](https://files.readme.io/2ec99e1-CleanShot_2024-04-23_at_15.37.542x.png)

**User > User's profile info has been updated**

This is required to keep the personal meeting ID of the user in sync.

![](https://files.readme.io/ac54de8-CleanShot_2024-04-23_at_15.38.072x.png)

## Add the event notification endpoint URL   [Skip link to Add the event notification endpoint URL](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#add-the-event-notification-endpoint-url)

Copy the webhook URL from your app in the dashboard:

![](https://files.readme.io/ae65b69dfdf632b249dcded526615cb6bb5732e53c228d9d768d2ed749f033e1-CleanShot_2024-11-11_at_16.39.132x.png)

Enter this in the **Event notification endpoint URL** and save the event subscription.

![](https://files.readme.io/bcf5027-CleanShot_2024-04-23_at_15.51.042x.png)

> ## ✅
>
> Your Zoom app is now set up for the Recall OAuth integration. Almost there!

# Recall vs customer managed OAuth   [Skip link to Recall vs customer managed OAuth](https://docs.recall.ai/docs/integration-guide-zoom-oauth\#recall-vs-customer-managed-oauth)

* * *

The next (and final) step is to implement the OAuth flow for your users in order to actually connect their Zoom accounts.

Once a user has gone through the OAuth flow, you can either manage access and refresh tokens on your end or have Recall manage these for you.

In general, we highly recommend using Recall-managed OAuth by default, unless:

- You already have an integration with the Zoom OAuth API.
- You need to call the Zoom API endpoints for other functionality in your app.

> ## ☑️  Before continuing
>
> Make sure you have these saved for the final step:
>
> - [ ]  Zoom App Client ID
> - [ ]  Zoom App Client Secret
> - [ ]  Zoom App Secret Token
> - [ ]  Recall Zoom OAuth App ID

Updated 6 months ago

* * *

Implement the OAuth Flow: Recall vs Customer-managed OAuth

- [Step 2: Recall-Managed OAuth](https://docs.recall.ai/docs/step-2-recall-managed-oauth)
- [Step 2 Alternative: Customer-Managed OAuth](https://docs.recall.ai/docs/step-2-alternative-customer-managed-oauth)

Did this page help you?

Yes

No

Ask AI