---
url: "https://docs.recall.ai/docs/bot-usage"
title: "Bot Usage"
---

Recall tracks usage as the duration the bot was active, starting from the `joining_call` event until the `done` event. This is because the usage is based on how long the bot server is running for

Bots are therefore billed for the time from `joining_call` event to the `done` event.

> ## 📘  Bot usage is **not** rounded
>
> Recall.ai doesn't round bot usage, and is prorated to the second.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/bot-usage\#faq)

## Does bot usage include the time the bot was in the waiting room?   [Skip link to Does bot usage include the time the bot was in the waiting room?](https://docs.recall.ai/docs/bot-usage\#does-bot-usage-include-the-time-the-bot-was-in-the-waiting-room)

Yes, bots are charged for the time it is in the waiting room. The bot is active during this time which is why its counted towards the bot's usage

Updated 5 days ago

* * *

Did this page help you?

Yes

No

Ask AI