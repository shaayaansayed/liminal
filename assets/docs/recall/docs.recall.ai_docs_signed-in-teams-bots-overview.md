---
url: "https://docs.recall.ai/docs/signed-in-teams-bots-overview"
title: "Overview"
---

By default the Teams bot will join meeting as an anonymous guest participant.

This means that, by default, MS Teams bots cannot join meetings which only allow signed in users or have [CAPTCHA enabled](https://learn.microsoft.com/en-us/microsoftteams/join-verification-check). If your bot is signed in to a Teams account and your domain is whitelisted by your customer's Teams tenant, your bot will be able to join calls without running into a CAPTCHA.

To overcome these limitations, you can configure your Teams bots to sign into a Microsoft account before joining a meeting.

# Important Considerations   [Skip link to Important Considerations](https://docs.recall.ai/docs/signed-in-teams-bots-overview\#important-considerations)

There are some important things to be aware of when using Microsoft Teams bots:

- **The bot name _cannot_ be overridden:** Signed in Teams bots get their name from the Teams account used to authenticate the bot, which overrides the `bot_name` parameter in [Create Bot](https://docs.recall.ai/reference/bot_create).
- **Signed in bots only work for [Business Microsoft Teams](https://recallai.readme.io/docs/personal-vs-business-ms-teams#business-ms-teams) meetings.**

> ## ⚠️  Personal MS Teams not supported
>
> Bots will fail to join Personal MS Teams links if mandatory login is enabled. While a vast majority of Teams meetings are using Business Teams, you should still be aware of this limitation if you have users that use the Personal version of MS teams.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/signed-in-teams-bots-overview\#faq)

* * *

## Will the bot _always_ sign into teams calls?   [Skip link to Will the bot ](https://docs.recall.ai/docs/signed-in-teams-bots-overview\#will-the-bot-always-sign-into-teams-calls)

This behavior is configurable according to your use case.

When settings up the credentials in the Recall dashboard, you can toggle this behavior using the **Login mandatory** checkbox:

![Login mandatory checkbox  If turned on, the bot will **always** sign in before joining Teams calls.   Otherwise, the bot will only sign in if required by the meeting.](https://files.readme.io/222be2c1804a9f95726250d77bd04b85ea81a3afcc6dc4157642ccfe690c2c54-CleanShot_2024-10-24_at_08.42.37.png)

Login mandatory checkbox

If turned on, the bot will **always** sign in before joining Teams calls.

Otherwise, the bot will only sign in if required by the meeting.

## Why do two bots signed in with the same account show up as only one attendee in Teams?   [Skip link to Why do two bots signed in with the same account show up as only one attendee in Teams?](https://docs.recall.ai/docs/signed-in-teams-bots-overview\#why-do-two-bots-signed-in-with-the-same-account-show-up-as-only-one-attendee-in-teams)

Teams merges participants that share the same email, so multiple bots using one account appear as a single attendee. Give each bot its own account to avoid this if you are testing with multiple signed-in teams bots

Updated 13 days ago

* * *

Did this page help you?

Yes

No

Ask AI