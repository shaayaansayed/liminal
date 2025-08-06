---
url: "https://docs.recall.ai/docs/zoom-3rd-party-recording-token"
title: "Zoom 3rd Party Recording Token"
---

> ## ❗️  A 3rd party recording token is a **closed beta** Zoom feature
>
> Before starting this, you must reach out to Zoom Support and ask them to enable the 3rd Party Recording Token feature **for both your Zoom app and the Zoom organization that owns your Zoom app**

The 3rd party recording token allows bots to join calls and start recording automatically, regardless of the user's local recording setting.

If a bot has 3rd party recording token access, there is no recording consent or recording notification presented by the Zoom client.

This is particularly useful for larger enterprises that cannot allow allow local recording for security purposes.

# Setup   [Skip link to Setup](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#setup)

* * *

In practice, implementing this feature is done through an account-level Zoom OAuth application, which is supported through Recall's [Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-oauth-integration).

> ## 📘  Native bots
>
> Currently, Zoom only supports this through the SDK used by [Zoom Native Bots](https://docs.recall.ai/docs/zoom-native-bots).
>
> More info on this can be found below.

## 1\. Create a Zoom Account-level OAuth App   [Skip link to 1. Create a Zoom Account-level OAuth App](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#1-create-a-zoom-account-level-oauth-app)

Create an account-level app by going to the [Zoom marketplace](https://marketplace.zoom.us/) and selecting **Develop > Build App**:

![](https://files.readme.io/fa2558c-CleanShot_2024-04-15_at_16.14.032x.png)

Select **General App**:

![](https://files.readme.io/33b47fa3a4deab2885c8d68dbf48f067d2db7339dec782541bb3766201dd53c7-CleanShot_2024-11-29_at_10.12.272x.png)

Make sure to configure the app to be admin-managed (account-level):

![_3rd party recording tokens are only available for **account-level** OAuth apps. _](https://files.readme.io/6b6630e-CleanShot_2024-04-15_at_16.15.002x.png)

_3rd party recording tokens are only available for **account-level** OAuth apps._

## 2\. Add scopes   [Skip link to 2. Add scopes](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#2-add-scopes)

Navigate to **Build your App > Scopes** and click **Add Scopes**

![](https://files.readme.io/4342abdc02245eb0412803fcb7d3a4b6455fb7c54c696731781409e1dd10a688-CleanShot_2024-11-29_at_10.26.352x.png)

Add the following scopes:

| Scope Name | Purpose |
| --- | --- |
| **`meeting_token:read:admin:3rdpartyrecording`** | This scope is used to retrieve the "3rd party recording token", which is provided to the bot to allow it to automatically begin recording without prompting the host for permission. |
| **`meeting:read:list_meetings:admin`** | This scope is used to enumerate all users' scheduled meetings, so that a 3rd party recording token can be generated when a bot is sent to one of their meetings. |
| **`user:read:list_users:admin`** | This scope is used to read the users' Personal Meeting ID (PMI), so that a 3rd party recording token can be generated when a bot is sent to their PMI. |

In the scope description, you should use the above to explain the purpose for each scope:

![](https://files.readme.io/1d26a4f1a934889fcd232ddfb69f51664803a7352f5c7cd11c9348fe4df8bd7b-CleanShot_2024-11-29_at_10.32.342x.png)

## 3\. Create the OAuth App in Recall   [Skip link to 3. Create the OAuth App in Recall](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#3-create-the-oauth-app-in-recall)

Copy the following app details:

- **Client ID**
- **Client Secret**
- **Webhook secret**

Your client ID and client secret can be found under **Build your app > Basic Information** or in the Application Credentials card in the top left.

The Zoom App Secret Token can be found under **Build your app > Features > Access**

![](https://files.readme.io/3b857c701ac996375e07e3f37f64915ce29b13ca1c389192ca9f8136d334609a-CleanShot_2024-11-29_at_11.10.552x.png)

Use these values to create the OAuth app in Recall.

This can be done through the API Explorer dashboard. Links for each region can be found below:

- [US (us-east-1)](https://us-east-1.recall.ai/dashboard/explorer/zoom-oauth)
- [EU (eu-central-1)](https://eu-central-1.recall.ai/dashboard/explorer/zoom-oauth)
- [Asia (ap-northeast-1)](https://ap-northeast-1.recall.ai/dashboard/explorer/zoom-oauth)
- [Pay-as-you-go (us-west-2)](https://us-west-2.recall.ai/dashboard/explorer/zoom-oauth)

Select Create App, fill out the app details, and click Create.

![](https://files.readme.io/6818c644ed3e568afe29242b91531a397eb6db3a5ff4fe165caa9620097668d9-CleanShot_2024-11-29_at_10.43.452x.png)

**Make sure to select Admin-managed.**

## 4\. Add the Zoom Event Subscription   [Skip link to 4. Add the Zoom Event Subscription](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#4-add-the-zoom-event-subscription)

View your newly created app. On the resource card, select more and copy the webhook URL:

![](https://files.readme.io/e3fbb4dc8cf125479bdc84acd452b3b121db23471ea73771970f694feead3964-CleanShot_2024-11-29_at_10.45.172x.png)

In your Zoom app, navigate to **Build your app > Features > Access**.

Toggle on **Event Subscription**, and click **Add a subscription**:

![](https://files.readme.io/b1564147779232cf3c04d398849adf0351694d811f8477b3b9865df65cabb7b2-CleanShot_2024-11-29_at_10.49.052x.png)

Paste the copied webhook URL into the **Event notification endpoint URL** field.

![](https://files.readme.io/78333ddc1d9ba21f1599553b55379a03ede58b121f13a10f87a737c1e9b220cf-CleanShot_2024-11-29_at_10.51.452x.png)

Click the **Add Events** button and add these two events:

**Meeting > Meeting has been created**

![](https://files.readme.io/2ec99e1-CleanShot_2024-04-23_at_15.37.542x.png)

**User > User's profile info has been updated**

![This is required to keep the personal meeting ID of the user in sync.](https://files.readme.io/ac54de8-CleanShot_2024-04-23_at_15.38.072x.png)

This is required to keep the personal meeting ID of the user in sync.

## 5\. Implement the OAuth flow   [Skip link to 5. Implement the OAuth flow](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#5-implement-the-oauth-flow)

Now that you have your app setup, the last step is to enable your users to authorize their accounts. The OAuth flow for the 3rd party recording token is the exact same as the normal Zoom OAuth integration, which you can find a guide for [here](https://docs.recall.ai/docs/recall-managed-oauth).

Once a Zoom account goes through this flow and connects your OAuth app, Recall will continually sync Zoom meetings for all users in the account. 3rd party tokens will automatically be provided for any of the synced Zoom meetings for the account, and bots will be able to record without local recording permissions.

## 6\. Request access and enable 3rd party recording   [Skip link to 6. Request access and enable 3rd party recording](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#6-request-access-and-enable-3rd-party-recording)

3rd party recording must be available and enabled on the Zoom account that will connect your app.

Before directing the Zoom admin through the OAuth flow, ensure 3rd party recording is available on their Zoom account.

They should also confirm this is enabled under: **Account Settings → Recording → Allow 3rd-party recording**

![](https://files.readme.io/532a2eb-zoom_3rd_party_recording_2.png)

Once they've gone through the OAuth flow and authorized their Zoom account, 3rd party recording tokens will automatically be provided for all of their bots.

# Bot configuration   [Skip link to Bot configuration](https://docs.recall.ai/docs/zoom-3rd-party-recording-token\#bot-configuration)

* * *

Since the 3rd party recording token is only supported by the [Zoom Native Bot](https://docs.recall.ai/docs/zoom-native-bots), if you're currently using the default Web bot, you'll need to add one additional parameter.

For bots using the 3rd party recording token, you **must** configure your [Create Bot](https://docs.recall.ai/reference/bot_create) requests to specify native Zoom bots by setting the `variant.zoom` parameter to `native`:

```rdmd-code lang- theme-light
curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header 'Authorization: {RECALLAI_API_KEY}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "variant": {
    "zoom": "native"
  },
  "meeting_url": "...",
  ...
}
'

```

Updated 5 months ago

* * *

Did this page help you?

Yes

No

Ask AI