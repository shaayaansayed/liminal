---
url: "https://docs.recall.ai/docs/microsoft-teams-bots-faq"
title: "Microsoft Teams: FAQ"
---

## Why does the bot have Unverified after the name?   [Skip link to Why does the bot have Unverified after the name?](https://docs.recall.ai/docs/microsoft-teams-bots-faq\#why-does-the-bot-have-unverified-after-the-name)

Microsoft released an [update](https://learn.microsoft.com/en-us/answers/questions/1534900/unverified-text-is-appearing-next-to-the-acs-user) February 2024 that affects how Teams participants are displayed depending on their account's relationship with the organization.

This only affects the new version of teams (teams.microsoft.com), and is not applicable for the old version (teams.live.com).

Below is a summary of these changes:

> **No label:** All participants who are part of the organizer’s organization.
>
> **External:** All participants who are external to the organizer’s organization but have a trusted relationship with the organizer or their organization.
>
> **Unverified:** All other participants will be seen with this label. This will include Microsoft Entra ID users who belong to organizations that do not have an explicit external access setup with the organizer’s organization, Microsoft Account (personal) users, users who are not using any Microsoft ID while joining meetings, and others.

This means that, by default, bot that join a Teams meetings hosted at teams.microsoft.com will have the `Unverified` suffix.

**How to remove the unverified tag**

If you wish to remove this tag in favor of the `(External)` tag, you can authenticate Teams bots as outlined in [Microsoft Teams Bot Login](https://docs.recall.ai/docs/microsoft-teams-bot-login-getting-started).

Microsoft Tenants can specify trusted organizations by following [these steps](https://learn.microsoft.com/en-us/microsoftteams/trusted-organizations-external-meetings-chat?tabs=organization-settings).

## How to bypass Microsoft Teams Captcha for Recall.ai Bots   [Skip link to How to bypass Microsoft Teams Captcha for Recall.ai Bots](https://docs.recall.ai/docs/microsoft-teams-bots-faq\#how-to-bypass-microsoft-teams-captcha-for-recallai-bots)

Your teams bots may encounter a `microsoft_teams_captcha_detected` error. This happens when the host's Teams organization has a few settings enabled that force untrusted participants to undergo additional (captcha) verification

To resolve this, you should implement [Signed-in Teams Bots](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams) and you can follow [this section](https://recall-knowledge-base.help.usepylon.com/articles/2427974610-configuring-microsoft-teams-settings-for-bot-access#how-to-add-your-bot-as-a-trusted-organization-to-bypass-captcha-21) to add a domain as a trusted organization

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI