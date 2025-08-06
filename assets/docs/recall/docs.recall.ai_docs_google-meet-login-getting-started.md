---
url: "https://docs.recall.ai/docs/google-meet-login-getting-started"
title: "Signed-In Google Google Meet Bots"
---

By default the Google Meet bot will join meeting as guest participant.

This can lead to limitations like:

1. Showing a warning message that the bot may not be who they claim to be
2. Not able to change avatar image
3. Not able to join meetings which only allow signed in users.

![1\. Unauthenticated Teams bot warning message](https://files.readme.io/fc570d2-CleanShot_2024-03-25_at_21.52.542x.png)

(1) Unauthenticated Teams bot warning message.

This warning can be uncomfortable for end users, especially if they don't understand it.

You can avoid this using Signed-in Google Meet bots.

In order to avoid these, Recall supports authenticating your Google Meet bots by providing them a set of configurable credentials before joining a meeting.

> ## 📘  Bot name **not** configurable
>
> Since authenticated Google meet bots get their name from the Google account used to authenticate the bot, this overrides the `bot_name` parameter in [Create Bot endpoint](https://docs.recall.ai/reference/bot_create).

# Setup   [Skip link to Setup](https://docs.recall.ai/docs/google-meet-login-getting-started\#setup)

* * *

## 1\. Create a Google Login Group   [Skip link to 1. Create a Google Login Group](https://docs.recall.ai/docs/google-meet-login-getting-started\#1-create-a-google-login-group)

A login group stores references to multiple logins(Google accounts). This allows Recall to perform a round robin allocation and avoid hitting concurrency limitations for authenticated accounts.

### (Recommended): Create the Login in the dashboard   [Skip link to (Recommended): Create the Login in the dashboard](https://docs.recall.ai/docs/google-meet-login-getting-started\#recommended-create-the-login-in-the-dashboard)

To create a Google Login Group, click the "Create Group" button on the Google Logins page in the explorer:

- [(US) us-east-1](https://us-east-1.recall.ai/dashboard/explorer/google-login)
- [(Pay-as-you-go) us-west-2](https://us-west-2.recall.ai/dashboard/explorer/google-login)
- [(EU) eu-central-1](https://eu-central-1.recall.ai/dashboard/explorer/google-login)
- [(JP) ap-northeast-1](https://ap-northeast-1.recall.ai/dashboard/explorer/google-login)

To control whether or not Meet bots should **always** sign in (vs. only when the meeting requires it), you can configure the `login_mode`:

![](https://files.readme.io/d12661871f84f11083a0591ad6cde3826504a720e93c23ed7c869fe0638f2c8f-CleanShot_2025-01-30_at_09.21.29.png)

**Alternative: Create the Login Group through the API:**

You can also use the [Create Login Group endpoint](https://docs.recall.ai/reference/google_login_groups_create) to add a login group.

- `name` \- Allows you to set a name to the login group (for e.g `Production Primary`)
- `login_mode` \- Set whether bots using this login group should always login or only if required.

**Example curl request:**

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v2/google-login-groups/ \
     --header 'Authorization: ${RECALL_API_KEY}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "login_mode": "always",
  "name": "Bot Group 1"
}
'

```

When the bot joins the call, it will use a login(Google account) (will be setup in Step 3) from the login group to authenticate itself.

## 2\. Create a new Google Workspace   [Skip link to 2. Create a new Google Workspace](https://docs.recall.ai/docs/google-meet-login-getting-started\#2-create-a-new-google-workspace)

The bot uses SSO based authentication and in order to proceed you need to create a [new dedicated Google Workspace](https://workspace.google.com/).

- You can use any domain, either a new domain that you register for this purpose, or a subdomain of your primary domain. For instance `sso.yourcompany.com`. **You cannot reuse your existing Google Workspace** if you already have one. The reason is because **this method relies on the organization-wide SSO policy which will break login for all accounts on your existing Google Workspace.**
- You can use email like `bot@sso.yourcompany.com` to sign up for the dedicated Google workspace.
- **You must have a paid workspace**, it can be on the cheapest (starter) tier. You can start with single user but may need to add more users depending on your concurrent bot usage.

### Setup SSO Profile   [Skip link to Setup SSO Profile](https://docs.recall.ai/docs/google-meet-login-getting-started\#setup-sso-profile)

1. Create an RSA private key and self-signed certificate. **Store these files somewhere safe! They will be needed in later steps**

```rdmd-code lang- theme-light
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes

```

2. In the Google Workspace admin dashboard, add a 3rd party SSO profile for the organization
1. In your Google Admin console (at admin.google.com)...


      Go to Menu and then Security > Authentication > SSO with third party IdP.

      _Requires having the Security settings administrator privilege._

2. In Third-party SSO profiles, click Add SAML profile.
      ![](https://files.readme.io/d6e7fa6c9c6049ed3898695f3d3ef624bc6dcf954414444799ea025958567e42-CleanShot_2024-11-27_at_11.01.102x.png)
3. At the bottom of the IdP details page, click **Go to legacy SSO profile settings.**

4. On the Legacy SSO profile page, check the **Enable SSO with third-party identity provider box**.

5. Setup redirect URLs
      1. Sign-in page URL: [https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-in](https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-in)
      2. Sign-out page URL: [https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-out](https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-out)
6. Verification certificate: Upload the `cert.pem` file created in step 1

7. Check " **Use a domain-specific issuer**"Scroll to the bottom and click " **Save**"
      ![](https://files.readme.io/a58080c9961d6d0fd613f90371d69134bc93aab6dad8156451e5d0cd5376f920-CleanShot_2024-11-27_at_10.48.132x.png)

3. Return to the **SSO with third-party IDPs page**.


Under **Manage SSO profile assignments**, click **Manage**:

![](https://files.readme.io/445fe4f10026fff65ce2217e3e82d5800345670a78c801e4443ea83e6b115729-CleanShot_2024-11-27_at_10.54.532x.png)


4. Select your Legacy SSO Profile from the dropdown and save:
![](https://files.readme.io/0da4b4421dc5d78a04425b83fc1615ed803d88b8ee0522d7e7f46bd4b20386cd-CleanShot_2024-11-27_at_10.58.10.gif)

## 3\. Create a Google Login   [Skip link to 3. Create a Google Login](https://docs.recall.ai/docs/google-meet-login-getting-started\#3-create-a-google-login)

Now you can start adding logins(Google accounts) to the login group(created in Step 1).

The easiest way to do this is in the explorer UI:

- [(US) us-east-1](https://us-east-1.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(Pay-as-you-go) us-west-2](https://us-west-2.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(EU) eu-central-1](https://eu-central-1.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(JP) ap-northeast-1](https://ap-northeast-1.recall.ai/dashboard/explorer/google-login?tab=logins)

You can also use the [Create Login Endpoint](https://docs.recall.ai/reference/google_logins_create):

- `group_id` \- Set this to the `id` of the login group created in Step 1.
- `sso_v2_workspace_domain` \- Set this to the domain of the Google workspace created in Step 2
- `sso_v2_private_key` \- Set this to the private key you generated in Step 2
- `sso_v2_cert` \- Set this to the cert you generated & uploaded in Step 2
- `email` \- Set this to the email account you created the Google workspace with (e.g `bot@sso.yourcompany.com`)
- `is_active` \- Set this to `true` to enable this login to be used by the login group.

**_Note: We recommend calling this endpoint using Postman, Insomnia, or a related tool, as cURL and the request sender in our docs are known to cause issues with PEM strings. Use form-data so you don't have to re-format the strings._**

Verify that the login has been successfully created using the [Retrieve Google Login Group endpoint](https://docs.recall.ai/reference/google_login_groups_retrieve). The `logins` field in response should include the login created above.

## 4\. Verify Bot Join Call   [Skip link to 4. Verify Bot Join Call](https://docs.recall.ai/docs/google-meet-login-getting-started\#4-verify-bot-join-call)

We have successfully setup a login group with an active login(Google account). Use the Create Bot endpoint to send a bot to a test Google Meet call and specify the login group id as `google_meet.google_login_group_id` parameter in the request. Also specify `google_meet.login_required` to force the bot to log in, even if it's not required to join the meeting, to ensure the bot uses the credentials to join your test meeting. You don't need to specify this parameter in normal usage.

1. You should receive the bot's request to join the call
2. The bot should have the name and profile picture which was setup when creating the new Google Workspace.
3. Additionally, you can invite the bot's email address (e.g `bot@sso.yourcompany.com`) to a Google Meet call. This will ensure the bot automatically joins the call instead of being in the waiting room.

## 5\. Adding more Logins   [Skip link to 5. Adding more Logins](https://docs.recall.ai/docs/google-meet-login-getting-started\#5-adding-more-logins)

> ## 🚧  Handling high login concurrency
>
> If a login group runs out of enabled ( `is_active`) Google logins (accounts) due to high concurrent usage the affected bots will produce a `fatal` event with `google_meet_login_not_available` as the sub code.
>
> **This indicates you need to add more Google Logins to the affected login group**.
>
> Each login supports roughly 30 concurrent logins, but we recommend you err on the side of caution when deciding on a number of logins to create.
>
> We recommend creating at least 3-4 logins to start, especially if you expect to have multiple bots joining the same call at any point.

To add more logins:

### Create a new user in the Google workspace   [Skip link to Create a new user in the Google workspace](https://docs.recall.ai/docs/google-meet-login-getting-started\#create-a-new-user-in-the-google-workspace)

Add a new user to the Google Workspace. Google has written [detailed steps](https://support.google.com/a/answer/33310?hl=en) to create a new user in your Google Workspace account.

### Create Login in Recall   [Skip link to Create Login in Recall](https://docs.recall.ai/docs/google-meet-login-getting-started\#create-login-in-recall)

The easiest way to do this is in the explorer UI:

- [(US) us-east-1](https://us-east-1.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(Pay-as-you-go) us-west-2](https://us-west-2.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(EU) eu-central-1](https://eu-central-1.recall.ai/dashboard/explorer/google-login?tab=logins)
- [(JP) ap-northeast-1](https://ap-northeast-1.recall.ai/dashboard/explorer/google-login?tab=logins)

You can also use the [Create Login Endpoint](https://docs.recall.ai/reference/google_logins_create) to add the login in Recall.

### Verify Multiple Logins   [Skip link to Verify Multiple Logins](https://docs.recall.ai/docs/google-meet-login-getting-started\#verify-multiple-logins)

To verify that all logins added to a login group work correctly, you can schedule multiple bots (same as the number of logins associated with a login group) to join a test Google Meet call at the same time(use the `join_at` parameter in the [Create Bot](https://docs.recall.ai/reference/bot_create) request).

> ## 📘
>
> **We recommend to configure all logins(Google accounts) belonging to a login group to have similar properties such as profile picture, account name etc**.

# Troubleshooting   [Skip link to Troubleshooting](https://docs.recall.ai/docs/google-meet-login-getting-started\#troubleshooting)

* * *

Check these things if signed-in Google Meet bots are failing to join calls.

## Check the language of the bot's Google account preferences   [Skip link to Check the language of the bot's Google account preferences](https://docs.recall.ai/docs/google-meet-login-getting-started\#check-the-language-of-the-bots-google-account-preferences)

Authenticated bots rely on language-sensitive context to join calls.

To ensure authenticated Google accounts can join calls, make sure the language is set to **_en-us_** by navigating to [https://myaccount.google.com/personal-info](https://myaccount.google.com/personal-info) and checking this setting:

**Personal info > General preferences for the web > Language** ➡️ _English (United States)_

![](https://files.readme.io/ea2a771-______.png)

_Other Questions? Check out the [Authenticated Bots FAQ](https://docs.recall.ai/docs/google-meet-faq)._

Updated 6 months ago

* * *

- [Google Meet FAQ](https://docs.recall.ai/docs/google-meet-faq)
- [Google Meet Overview](https://docs.recall.ai/docs/google-meet)

Did this page help you?

Yes

No

Ask AI