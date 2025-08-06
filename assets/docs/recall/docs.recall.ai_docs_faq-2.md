---
url: "https://docs.recall.ai/docs/faq-2"
title: "Slack Huddles FAQ"
---

## 1\. Can the Slack Bot join multiple huddles at once?   [Skip link to 1. Can the Slack Bot join multiple huddles at once?](https://docs.recall.ai/docs/faq-2\#1-can-the-slack-bot-join-multiple-huddles-at-once)

Yes, the slack bot is able to join concurrent huddles. We have not observed a maximum threshold for the number of simultaneous huddles but we will alert you if we discover one.

## 2\. How does the Slack Bot decide which huddles to join?   [Skip link to 2. How does the Slack Bot decide which huddles to join?](https://docs.recall.ai/docs/faq-2\#2-how-does-the-slack-bot-decide-which-huddles-to-join)

This is configurable based on the parameters in the [Create Slack Team Integration](https://recallai.readme.io/reference/slack_teams_create) endpoint. At a high-level you can configure the bot to automatically join public huddles or filter huddles to a specific user or set of users.

## 3\. Can the Slack Bot join private huddles?   [Skip link to 3. Can the Slack Bot join private huddles?](https://docs.recall.ai/docs/faq-2\#3-can-the-slack-bot-join-private-huddles)

Yes, but it needs to be invited by a participant of the huddle. We also have an option to prompt users in private huddles with a message if the bot notices they are in a huddle.

## 4\. Can I control the appearance of the bot?   [Skip link to 4. Can I control the appearance of the bot?](https://docs.recall.ai/docs/faq-2\#4-can-i-control-the-appearance-of-the-bot)

Yes, you can control the name and profile picture the Slack Bot.

## 5\. Why do I need to go through the domain setup process?   [Skip link to 5. Why do I need to go through the domain setup process?](https://docs.recall.ai/docs/faq-2\#5-why-do-i-need-to-go-through-the-domain-setup-process)

In order to authenticate the bot, the bot needs to be able to receive emails from Slack. We automate this process for you so you do not have to worry about it, but you will need to bring a domain in order to receive the emails.

## 6\. When is Slack admin approval required?   [Skip link to 6. When is Slack admin approval required?](https://docs.recall.ai/docs/faq-2\#6-when-is-slack-admin-approval-required)

Most often, an admin approval is required to invite the bot because it has a different email domain than the domain of the end-users customer. This approval is only required once to invite the bot. Then the bot is able to join huddles without approval.

## 7\. Why does the Slack Bot need to be added as a participant?   [Skip link to 7. Why does the Slack Bot need to be added as a participant?](https://docs.recall.ai/docs/faq-2\#7-why-does-the-slack-bot-need-to-be-added-as-a-participant)

When adding an account to your slack, there are 3 options:

- Single-channel guest
- Multi-channel guest
- Participant (User)

Single-channel guests can only see one channel and they don't know when slack huddles are happening in other channels. This prevents them from joining slack huddles automatically.

Multi-channel guests are like single channel guests, but they can be added to a multiple number of specified channels. You could _technically_ add a multi-channel guest to every single channel, but multi-channel guests are billed the same as actual users, and ultimately this would mean having to manually add them to every single new channel.

In summary, guests in a Slack workspace are not able to see the contents of other channels, including when huddles are started in them. Thus, in order for the bot reasonably be able to join slack huddles automatically, they must be added as a participant in your Slack workspace.

Note that when it comes to Slack Billing, this bot will be treated as an additional Slack seat.

## 8\. How do I know which users were in a Slack huddle?   [Skip link to 8. How do I know which users were in a Slack huddle?](https://docs.recall.ai/docs/faq-2\#8-how-do-i-know-which-users-were-in-a-slack-huddle)

We include the user's slack ID and email (if available) in the participant metadata field.

You can use the Slack ID (recommended) or email to tie the recordings back to individual users in your system.

Updated6 months ago

* * *

Did this page help you?

Yes

No

Ask AI