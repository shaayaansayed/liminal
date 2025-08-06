---
url: "https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started"
title: "Setup Guide"
---

By default the Teams bot will join meeting as guest participant. This can lead to bot not able to join meetings which only allow signed in users.

Recall supports authenticated Teams bot participant bot will sign in using credentials before joining a meeting.

> ## 📘  Bot name cannot be overridden
>
> One important caveat to using signed-in Microsoft Teams bots is that they get their name from the Microsoft Teams account used to authenticate the bot.
>
> This overrides the `bot_name` parameter in [Create Bot endpoint](https://docs.recall.ai/reference/bot_create).

Follow these steps to setup authenticated bots for Microsoft Teams.

# 1\. Setup Microsoft Account   [Skip link to 1. Setup Microsoft Account](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#1-setup-microsoft-account)

_Since the authenticated bot requires global organization-level permission changes, authenticated Teams bots should always use a new Microsoft account_

## Select an account type   [Skip link to Select an account type](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#select-an-account-type)

Create a new Microsoft 365 account. This **must** be a paid account. You can start by signing up for Microsoft 365 Business Basic plan from here [https://www.microsoft.com/en-us/microsoft-365/business#heading-ocb6f5](https://www.microsoft.com/en-us/microsoft-365/business#heading-ocb6f5)

![](https://files.readme.io/74a2222-microsoft365_business_signup.png)

- You will be able to choose the account username in follow up steps. For setup purpose you can proceed with `.onmicrosoft.com` domain. This can be later configured to be on a custom domain as well.

![](https://files.readme.io/5a12b17-username_setup.png)

- Post signup you will be redirected to account setup wizard. Follow the steps to finish it. This will allow you to add a custom domain to your Microsoft Business Account (if required)

# 2\. Update Security Settings   [Skip link to 2. Update Security Settings](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#2-update-security-settings)

In order for the bot to be able to login seamlessly MFA and other security settings **must be turned off** for your account. These are listed below:

### 2.1 Disable Security defaults   [Skip link to 2.1 Disable Security defaults](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#21-disable-security-defaults)

- With your new Microsoft account logged in, visit [https://portal.azure.com/#home](https://portal.azure.com/#home)
- Open `Microsoft Entra ID` from sidebar

![](https://files.readme.io/ce7e253-open_entra_id.png)

- Select `Manage Security Defaults` from `Overview -> Properties`
- Disable security defaults

![](https://files.readme.io/513918f-disable_security_defaults.png)

### 2.2 Disable "Show keep user signed in" prompt   [Skip link to 2.2 Disable "Show keep user signed in" prompt](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#22-disable-show-keep-user-signed-in-prompt)

- With your new Microsoft account logged in, visit [https://portal.azure.com/#home](https://portal.azure.com/#home) and Open `Microsoft Entra ID` from sidebar.
- Select `Users -> User settings` from sidebar
- Disable `**Show keep user signed in**` prompt

![](https://files.readme.io/612962f-disable_keep_user_signed_in.png)

### 2.3 Update account data   [Skip link to 2.3 Update account data](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#23-update-account-data)

- With your new Microsoft account logged in, visit [https://portal.azure.com/#home](https://portal.azure.com/#home) and Open `Microsoft Entra ID` from sidebar.
- Change user properties for e.g name, profile picture etc by selecting user from `All Users` list in `Users` section

![](https://files.readme.io/89f6f14-Screenshot_2023-11-16_at_4.04.07_PM.png)

### 2.4 Verify Teams access   [Skip link to 2.4 Verify Teams access](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#24-verify-teams-access)

- With your new Microsoft account logged in, visit [https://teams.microsoft.com](https://teams.microsoft.com/)
- Complete onboarding wizard and verify that you are able to start a Teams call from the dashboard

![](https://files.readme.io/448f0e8-Screenshot_2023-11-16_at_4.07.45_PM.png)

# 3\. Configure credentials in Recall dashboard   [Skip link to 3. Configure credentials in Recall dashboard](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started\#3-configure-credentials-in-recall-dashboard)

Once you've setup the account, the last step is to configure it in the Recall dashboard [here](https://api.recall.ai/dashboard/platforms/teams-web). **We recommend doing this step first on your development/staging account before applying to your production Recall account.**

Add the `username` & `password` for the account under the Teams Web Credentials tab.

![](https://files.readme.io/b6037ea-Screenshot_2023-11-16_at_4.12.49_PM.png)

> ## 🚧  We recommend keeping Login Mandatory option turned off.
>
> The login mandatory option (if turned on) forces the bot to always login before joining the call. Due to authentication flow for Teams web this can lead to increased delay in bots joining call. We recommend to keep this option off, as a result bot will attempt to login only for calls where signed in participants are mandatory

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI