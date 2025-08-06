---
url: "https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams"
title: "Setting up Signed-in Bots for Microsoft Teams"
---

**This guide is for you if:**

- You need to join meetings that only allow signed-in Microsoft teams users

**Limitations:**

- _Signed-in bot names cannot be overridden_ \- Signed-in Microsoft Teams bots get their name from the Microsoft Teams account used to sign-in the bot. This overrides the `bot_name` parameter in [Create Bot endpoint](https://docs.recall.ai/reference/bot_create)
- _Signed-in Microsoft Teams bots must be in their own Organization_ \- Signed-in Microsoft Teams bots must be in their own organization due to global organization-level permission changes

# Signed-in Microsoft Teams Bot in 5 Steps   [Skip link to Signed-in Microsoft Teams Bot in 5 Steps](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#signed-in-microsoft-teams-bot-in-5-steps)

In this guide, you will:

1. **Create a new Microsoft Teams Business Organization and Account**. The only user in this organization is the bot account
2. **Update the Account Security Settings**. The account is now able to seamlessly join meetings without needing to 2FA or store sessions
3. **Update your Account Profile**. The bot account is customized and will reflect that when in meetings
4. **Add your Microsoft Account Credentials to Recall**. Now Recall is able to sign in your bot on behalf of the new account/organization you've made
5. **See the bot in action**. You have tested the bot and it is working as flawlessly

Let's get started 👇

## Step 1: Create a new Microsoft Business Organization   [Skip link to Step 1: Create a new Microsoft Business Organization](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-1-create-a-new-microsoft-business-organization)

> ## ❗️  Do not create the bot account in your existing Microsoft business organization
>
> Since the authenticated bot **requires global organization-level permission changes**, authenticated Teams bots should always use a new Microsoft account

### Step 1.1: Choose the `Microsoft 365 Business Basic` Plan   [Skip link to Step 1.1: Choose the ](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-11-choose-the-microsoft-365-business-basic-plan)

**Quick Note: This must be a paid account**. The Microsoft 365 Business Basic account is $6USD/month and has the minimum required features needed.

To get started, head to the [Microsoft 365 Business Pricing Page](https://www.microsoft.com/en-us/microsoft-teams/compare-microsoft-teams-business-options) to create a new account.

![](https://files.readme.io/e9476ed1d12896a6d5c25e0b94af5d7eb9207cf6d6cc101aea6122fbb56e4aac-CleanShot_2025-03-26_at_08.29.48.png)

### Step 1.2: Complete your account and organization registration   [Skip link to Step 1.2: Complete your account and organization registration](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-12-complete-your-account-and-organization-registration)

After selecting the plan, complete the account information, organization information, and payment steps.

You'll notice that the email uses the `@*.onmicrosoft.com` domain. This can be later configured to be a custom domain as well if needed.

![The red box highlights the auto-generated email domain. This domain can be updated to a custom domain from the dashboard later](https://files.readme.io/5a12b17-username_setup.png)

The red box highlights the auto-generated email domain. This domain can be updated to a custom domain from the dashboard later

### Checkpoint   [Skip link to Checkpoint](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#checkpoint)

At this point, you should be in the dashboard with a new organization and Microsoft Teams Business email account

## Step 2: Update Organization Security Settings   [Skip link to Step 2: Update Organization Security Settings](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-2-update-organization-security-settings)

The goal of this step is to allow the bot to seamlessly join meetings without having to go through 2FA and other security measures which is enforced by Microsoft Teams Business by default. We will do this by updating the security settings to only use the minimum-required configurations

### Step 2.1: Disabling Security Defaults   [Skip link to Step 2.1: Disabling Security Defaults](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-21-disabling-security-defaults)

While signed into the bot Microsoft Teams Business account, head to the [Azure Dashboard](https://portal.azure.com/#home). Then search for the `Microsoft Entra ID` product

Once in the `Microsoft Entra Id` product, disable the security defaults found in `Overview > Properties > Manage Security Defaults` and set `Security Defaults` to `Disabled (not recommended)`. All tabs and fields can be seen in the image below

![Navigating to the Security Defaults dropdown. Make sure this field is disabled](https://files.readme.io/9cee5eb0b51c26c5d7c03624fae2657e471149accffafac50bd3c7d39c1c16f2-CleanShot_2024-12-05_at_18.34.212x.png)

Navigating to the Security Defaults dropdown. Make sure this field is disabled

### Step 2.2: Disable "Show keep user signed in"   [Skip link to Step 2.2: Disable "Show keep user signed in"](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-22-disable-show-keep-user-signed-in)

While signed into the bot Microsoft Teams Business account, head to the [Azure Dashboard](https://portal.azure.com/#home). Then search for the `Users` product.

Once in the `Users` product, click on `User Settings` in the sidebar and disable the "Show keep users signed in" toggle. The path and toggle can be seen in the image below

![Navigating to the "Show keep user signed in" toggle. Make sure this toggle is off](https://files.readme.io/4ea50509a693e48c7c2250bf4b75b1923e676a3a56a7453958160b2ce92e3802-CleanShot_2024-12-05_at_18.45.582x.png)

Navigating to the "Show keep user signed in" toggle. Make sure this toggle is off

### Checkpoint   [Skip link to Checkpoint](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#checkpoint-1)

At this point, you should have disabled "Security Defaults" and turned off the "Show keep user signed in" toggle. This will skip 2FA and will make sure your bot sessions expire after the bot leaves the call

## Step 3: Customize the bot profile   [Skip link to Step 3: Customize the bot profile](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-3-customize-the-bot-profile)

This step will update the bot details seen in the meeting itself. You can update the display name and profile image here

> ## 🚧  The bot display name and profile image cannot be overridden
>
> Regardless of what you specify in your [Create Bot](https://docs.recall.ai/reference/bot_create) request, the display name and profile photo will always be taken from the Microsoft account details defined in this section

### Step 3.1: Update the account details   [Skip link to Step 3.1: Update the account details](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-31-update-the-account-details)

While signed into the bot Microsoft Teams Business account, head to the [Azure Dashboard](https://portal.azure.com/#home). Then search for the `Users` product

Once in the users product, select the bot profile you want to update

![Navigating to your bot account](https://files.readme.io/9471dd748668d664e0fe9b66ba9699673c220d30da2a8d39d2d0b20b497867e1-CleanShot_2024-12-05_at_18.59.482x.png)

Navigating to your bot account

After selecting your profile, update the "Display Name" and "Profile Image" to reflect what you want to display in meetings

![Click the "Camera icon" to update the profile image and "Edit properties" to update the Display Name](https://files.readme.io/1c52374441a5631e53a4bff8eccd46b96d86172d4eaf4d0abf8373e47d211e67-CleanShot_2024-12-05_at_19.02.282x.png)

Click the "Camera icon" to update the profile image and "Edit properties" to update the display name

### Step 3.3: Login to Microsoft Teams and Start Test Call   [Skip link to Step 3.3: Login to Microsoft Teams and Start Test Call](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-33-login-to-microsoft-teams-and-start-test-call)

After your account is set up, head to [Microsoft Teams](https://teams.microsoft.com/). Once there, login with your account and complete the onboarding process. We also recommend trying to create a new call to make sure your Display Name and Profile Image are what you are expecting

### Checkpoint   [Skip link to Checkpoint](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#checkpoint-2)

At this point, you should have your display name and profile photo updated on the account your bot will impersonate in meetings

## Step 4: Add the Microsoft Teams Business Account Email & Password in the Recall Dashboard   [Skip link to Step 4: Add the Microsoft Teams Business Account Email & Password in the Recall Dashboard](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-4-add-the-microsoft-teams-business-account-email--password-in-the-recall-dashboard)

As the title says, [head over to Recall and login](https://www.recall.ai/login). Make sure you select the right region when logging in.

Once in the recall dashboard, update your Microsoft Teams Business Account login credentials in `Teams Web Credentials`

![Navigating to the Microsoft Teams Web Credentials (Microsoft Teams Business Account Credentials)](https://files.readme.io/e15b7d1b5f4f45cea8404dfa2d9a3e14a53b8dd4a3d379120792f6e1b476022e-CleanShot_2024-12-05_at_19.09.482x.png)

Navigating to the Microsoft Teams Web Credentials (Microsoft Teams Business Account Credentials)

In your Teams Web Credentials, add your login credentials and click the Create Configuration button

![Save your Microsoft Teams Business Account email and password for recall to use when joining meetings](https://files.readme.io/96c7183be82e3b975aaf30dd8329dcb2aa37aed4746cd5cf330adbb81550abc1-CleanShot_2024-12-05_at_19.12.452x.png)

Save your Microsoft Teams Business Account email and password for recall to use when joining meetings

> ## 🚧  We recommend keeping Login Mandatory option turned off.
>
> The login mandatory option (if turned on) forces the bot to always login before joining the call. Due to authentication flow for Teams web this can lead to increased delays before bots join the call. We recommend to keep this option off, as a result bot will attempt to login only for calls where signed in participants are mandatory

### Checkpoint   [Skip link to Checkpoint](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#checkpoint-3)

By this point, you should have your Microsoft Teams Business Account login credentials saved in recall

## Step 5: Test the bot   [Skip link to Step 5: Test the bot](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#step-5-test-the-bot)

Now that your new bot account is set up, you can try sending your bot to a new Microsoft Teams meeting

You can quickly test this by sending a bot using the interactive [Create Bot](https://docs.recall.ai/reference/bot_create) api docs. Make sure you use a new Teams Meeting URL and the API key from the Recall account with your Microsoft Teams Business Account login credentials

Note that you the bot will only sign in for meetings that require signed-in participants

## Wrapping up   [Skip link to Wrapping up](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#wrapping-up)

Hooray! By this point you have:

1. **Created a new Microsoft Teams Business Organization and Account**. The only user in this organization is the bot account
2. **Updated the Account Security Settings**. The account is now able to seamlessly join meetings without needing to 2FA or store sessions
3. **Updated your Account Profile**. The bot account is customized and will reflect that when in meetings
4. **Added your Microsoft Account Credentials to Recall**. Now Recall is able to sign in your bot on behalf of the new account/organization you've made
5. **Seen the bot in action**. You have tested the bot and it is working as flawlessly

Good work and if you have any questions, don't hesitate to reach out to us at **[support@recall.ai](mailto:support@recall.ai)**

# FAQs   [Skip link to FAQs](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#faqs)

## Why does the bot sometimes have `(Guest)` and others `(External)` after the display name?   [Skip link to Why does the bot sometimes have ](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#why-does-the-bot-sometimes-have-guest-and-others-external-after-the-display-name)

A bot has `(Guest)` next to the display name when the bot is not signed in.

A bot has `(External)` next to the display name when the bot is signed in.

If you want the bot to always show `(External)` instead of `(Guest)`, you can enable the "Login Mandatory" checkbox in the Teams Web Credentials. **Note that logging in the bots take a significantly longer time to join calls**

## Why does the bot have `(Unverified)` after the display name?   [Skip link to Why does the bot have ](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#why-does-the-bot-have-unverified-after-the-display-name)

Microsoft released an [update](https://learn.microsoft.com/en-us/answers/questions/1534900/unverified-text-is-appearing-next-to-the-acs-user) February 2024 that affects how Teams participants are displayed depending on their account's relationship with the organization.

This only affects the new version of teams (teams.microsoft.com), and is not applicable for the old version (teams.live.com).

Below is a summary of these changes:

> **No label:** All participants who are part of the organizer’s organization.
>
> **External:** All participants who are external to the organizer’s organization but have a trusted relationship with the organizer or their organization.
>
> **Unverified:** All other participants will be seen with this label. This will include Microsoft Entra ID users who belong to organizations that do not have an explicit external access setup with the organizer’s organization, Microsoft Account (personal) users, users who are not using any Microsoft ID while joining meetings, and others.

This means that, by default, bot that join a Teams meetings hosted at teams.microsoft.com will have the `Unverified` suffix.

## Would Microsoft Teams Essentials plan also work for setting this up or does this requires a Microsoft 365 Business Basic?   [Skip link to Would Microsoft Teams Essentials plan also work for setting this up or does this requires a Microsoft 365 Business Basic?](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#would-microsoft-teams-essentials-plan-also-work-for-setting-this-up-or-does-this-requires-a-microsoft-365-business-basic)

We haven't tested the Microsoft Teams Essentials plan ourselves so we can't say for certain but we recommend our devs use the Microsoft 365 Business Basic plan as this is what we used for setup and it contains all the required security settings and configurations needed for the bot to join calls

## Is there a way to detect beforehand when a Signed-in Teams bot will be required for a user meeting   [Skip link to Is there a way to detect beforehand when a Signed-in Teams bot will be required for a user meeting](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#is-there-a-way-to-detect-beforehand-when-a-signed-in-teams-bot-will-be-required-for-a-user-meeting)

There is not a way for you to detect what kind of bot will be required for a meeting beforehand because the bot will need to attempt to sign in and encounter the "you need to sign in" page for us to know

That being said, we also have an option in the dashboard to make the bot sign in for every meeting (called "Login Mandatory"). If you leave this bot unchecked, it will only sign in for meetings that require participant sign-in

We generally recommend developers leave this box unchecked (do not sign in for every meeting, only when required) to keep the bot's join time as low as possible

## Can we use our own Teams organization or do we need a new Teams organization for every customer?   [Skip link to Can we use our own Teams organization or do we need a new Teams organization for every customer?](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#can-we-use-our-own-teams-organization-or-do-we-need-a-new-teams-organization-for-every-customer)

We recommend creating a new organization for the bot, then all of your customers can invite this bot to their org (so you only need one new org for all your customers). We recommend creating a new organization for your bot because you need to update the org's security settings which you typically don't want to apply to your whole org

We also recommend having your customers tenants add the bots domain as a "trusted organization" in their security settings

## Will Signed-in Teams bots work for Calendar V1, V2, scheduled bots, or ad-hoc bots?   [Skip link to Will Signed-in Teams bots work for Calendar V1, V2, scheduled bots, or ad-hoc bots?](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams\#will-signed-in-teams-bots-work-for-calendar-v1-v2-scheduled-bots-or-ad-hoc-bots)

This will work for all meetings (calendar v1/v2 meetings, scheduled meetings, or adhoc meetings). Once you configure it in the Recall dashboard, this gets applied to all your Teams bots moving forward

Updated 4 months ago

* * *

Did this page help you?

Yes

No

Ask AI