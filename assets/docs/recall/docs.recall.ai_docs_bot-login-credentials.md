---
url: "https://docs.recall.ai/docs/bot-login-credentials"
title: "Bot Login Credentials"
---

> ## ❗️  This method for setting up authenticated Google Meet bots has been deprecated. Please refer to the guide in below link to setup authenticated Google Meet bots:
>
> [Setup Authenticated Google Meet Bot](https://docs.recall.ai/docs/google-meet-login-getting-started)

By default the Google Meet bot joins every meeting as a guest participant. This can lead to certain limitations (e.g not having a configurable avatar).

In order to avoid, Recall supports authorized Google Meet bot participant i.e bots will be able to sign in using configurable credentials before joining a meeting.

## Creating Bot Account   [Skip link to Creating Bot Account](https://docs.recall.ai/docs/bot-login-credentials\#creating-bot-account)

1. Use a fresh google account for the bot.
2. Ensure to set both **recovery email** & **recovery phone number** on the bot account. Failure to do so can result in the bot running into "BOT\_SIGN\_IN\_FAILED" errors.
3. Ensure the bot account language is set to **English(US)**.

## How login credentials work   [Skip link to How login credentials work](https://docs.recall.ai/docs/bot-login-credentials\#how-login-credentials-work)

1. If `Login Mandatory` is turned on, the bot will login with the credentials before joining every call.
2. If `Login Mandatory` is turned off, the bot will only attempt to login for calls that require the participants to be signed in.
3. The `bot_name` field does not work for logged in bots as Google Meet does not support customising name for logged in participants.

## Login Methods   [Skip link to Login Methods](https://docs.recall.ai/docs/bot-login-credentials\#login-methods)

![](https://files.readme.io/a07ae06-image.png)

There are several methods that the bot can use to log-in. Each method requires it's own set of credentials, and these can be configured in the dashboard under the [Google Meet Credentials tab](https://api.recall.ai/dashboard/platforms/gmeet).

### SSO V2 (Green Box) (Recommended)   [Skip link to SSO V2 (Green Box) (Recommended)](https://docs.recall.ai/docs/bot-login-credentials\#sso-v2-green-box-recommended)

This is currently the recommended method to have Google Meet bots sign in to the call. This method is the fastest and most reliable sign-in method.

You can set up SSO V2 using the following steps:

1. Create a dedicated Google Workspace that contains a bot user.
1. You must have a paid workspace, it can be on the cheapest (starter) tier and only needs one user account
2. You can use any domain, either a new domain that you register for this purpose, or a subdomain of your primary domain. For instance `sso.yourcompany.com`.
3. **You cannot reuse your existing Google Workspace if you already have one.** The reason is because this method relies on the organisation-wide SSO policy which could break your existing Google accounts.
2. Configure an user in your workspace which the bot will authenticate as.
1. Fill **username** field in the dashboard with the email address of the bot account. For e.g if the bot's account is `bot@sso.yourcompany.com` then **username = [bot@sso.yourcompany.com](mailto:bot@sso.yourcompany.com)**. **Incorrect username value will cause the bot to be stuck in joining\_call state**.
2. **The bot will join the meetings using the name of this google account, you can specify the name to be what makes sense for your use case.**
3. This will override the `bot_name` parameter in [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint, this is a limitation of authenticated Google Meet bots.
3. Ensure you login to the user account at least once, in order to accept the new account disclaimer.


![](https://files.readme.io/4f82faa-image_3.png)

2. **If you skip this step the bot will get stuck in the `joining_call` state**
3. Create an RSA private key and self-signed certificate: `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes`. Store these files somewhere safe!
4. In Google Workspace admin, set up an SSO profile for the organisation:


![](https://files.readme.io/b561cfa-Screenshot_2023-07-13_at_2.21.29_pm.png)

![](https://files.readme.io/2952082-Screenshot_2023-07-13_at_2.28.35_pm.png)

3. Check " _Set up SSO with third-party provider_"

1. _Sign-in page URL:_ `https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-in`
2. _Sign-out page URL:_ `https://us-east-1.recall.ai/api/v1/bot/gmeet-sign-out`
3. _Verification certificate_: Upload the `cert.pem` file created in step 3
4. Check " _Use a domain-specific issuer_"
5. Scroll to the bottom and click " _Save_"
4. Back in your Recall Dashboard: [https://us-east-1.recall.ai/dashboard/platforms/gmeet](https://us-east-1.recall.ai/dashboard/platforms/gmeet) fill out the following

1. _SSO V2 - Google Workspace Domain:_ the domain of your google workspace, eg `sso.yourcompany.com`
2. _SSO V2 - Private Key (PEM):_ the `key.pem` file created in step 3
3. _SSO V2 - Certificate (PEM):_ the `cert.pem` file created in step 3
4. _Login Mandatory_: check this box

### Username/Password (Red Box)   [Skip link to Username/Password (Red Box)](https://docs.recall.ai/docs/bot-login-credentials\#usernamepassword-red-box)

This is the most basic and straightforward sign-in method, where the bot uses the username and password of the Google account to sign in. However this method is the slowest, and can sometimes fail if Google rejects the request or displays a CAPTCHA.

You can setup Username/Password sign-in through the following steps:

1. Create a new Google Account for the bot, and note the username, password, recovery email and recovery phone number.
2. Input these values in the Recall Dashboard

### SSO V1 (Blue Box)   [Skip link to SSO V1 (Blue Box)](https://docs.recall.ai/docs/bot-login-credentials\#sso-v1-blue-box)

Deprecated - please use SSO V2 above.

#### Migration from SSO V1   [Skip link to Migration from SSO V1](https://docs.recall.ai/docs/bot-login-credentials\#migration-from-sso-v1)

If you currently have bots signing in using SSO V1, you will want to temporarily disable SSO by unchecking Login Mandatory in your Recall Dashboard before the cutover.

This is so your existing bots do not fail to authenticate using the SSO V1 method after you change the signing certificate in your Google Workspace.

Updated 12 months ago

* * *

Did this page help you?

Yes

No

Ask AI