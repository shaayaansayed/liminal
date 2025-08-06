---
url: "https://docs.recall.ai/docs/bot-status-change-events"
title: "Bot Webhooks"
---

Recall uses bot status changes to capture the lifecycle of a bot.

These status changes are exposed through webhooks, which your application can use to create a real-time experience or react to asynchronous events outside of the API request cycle.

For example, you may want to update something on your end when a bot transitions its status from `joining_call` to `in_call_recording`. When these asynchronous events happen, we'll make a POST request to the address you give us and you can do whatever you need with it on your end.

After a webhook is configured for an environment, notifications will be sent for all events for that environment.

> ## 🚧  Important webhook handler considerations
>
> - **`2xx` response:** Your webhook handler should return a HTTP `2xx` Code
> - **Retries:** If Recall doesn't receive a `2xx` response from your server, we will continue to try the message for the next 24 hours, with an increasing delay between attempts.
> - **Timeouts:** Webhook events have a timeout of 15 seconds. If you plan to kick off longer running tasks upon receiving certain events, make sure to do this asynchronously so you respond to requests before they time out.

## Events   [Skip link to Events](https://docs.recall.ai/docs/bot-status-change-events\#events)

This webhook is sent whenever the bot's status is changed and is delivered via Svix to the endpoints configured in your [Recall dashboard](https://api.recall.ai/dashboard/webhooks/).

JSON

```rdmd-code lang-json theme-light

{
  "event": "bot.joining_call",
  // bot.in_waiting_room, bot.in_call_not_recording, bot.recording_permission_allowed
  // bot.recording_permission_denied, bot.in_call_recording, bot.call_ended
  // bot.done, bot.fatal
  "data": {
    "data": {
      "code": string,
      "sub_code": string | null,
      "updated_at": string
    },
    "bot": {
      "id": string,
      "metadata": object
    }
  }
}

```

| Event | Description |
| --- | --- |
| `bot.joining_call` | The bot has acknowledged the request to join the call, and is in the process of connecting. |
| `bot.in_waiting_room` | The bot is in the waiting room of the meeting. |
| `bot.in_call_not_recording` | The bot has joined the meeting, however is not recording yet. This could be because the bot is still setting up, does not have recording permissions, or the recording was paused. |
| `bot.recording_permission_allowed` | The bot has joined the meeting and it's request to record the meeting has been allowed by the host. |
| `bot.recording_permission_denied` | The bot has joined the meeting and it's request to record the meeting has been denied. Refer to the `data.sub_code` for the exact reason. |
| `bot.in_call_recording` | The bot is in the meeting, and is currently recording the audio and video. |
| `bot.call_ended` | The bot has left the call, and the real-time transcription is complete.<br>The `data.sub_code` will contain machine readable code for why the call ended. |
| `bot.done` | The bot has shut down. If bot produced `in_call_recording` event, the video is uploaded and available for download. |
| `bot.fatal` | The bot has encountered an error that prevented it from joining the call. The `data.sub_code` will contain machine readable code for why bot failed. |

> ## 🚧  We may add additional Status Change event codes
>
> You should not treat the `data.code` and `data.sub_code` as an enum, as we may add values in the future without prior notice. We will never remove values without notifying all our customers and a long depreciation period, as we consider removing values a breaking change.

The list of `sub_code` & corresponding descriptions can be found here [here](https://docs.recall.ai/docs/sub-codes#fatal-sub-codes).

## Bot Status Transition Diagram   [Skip link to Bot Status Transition Diagram](https://docs.recall.ai/docs/bot-status-change-events\#bot-status-transition-diagram)

This diagram provides a detailed view of bot statuses:

![](https://files.readme.io/17216cb-Bot_Status_Transition_Flow_Chart.png)

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/bot-status-change-events\#faq)

* * *

## Where do I find my signing secret?   [Skip link to Where do I find my signing secret?](https://docs.recall.ai/docs/bot-status-change-events\#where-do-i-find-my-signing-secret)

Head over to the [Recall webhooks dashboard](https://api.recall.ai/dashboard/webhooks/) and click into the endpoint.

You'll find the signing secret near the bottom right hand corner:

![](https://files.readme.io/f7dd3b4-CleanShot_2024-01-14_at_21.51.202x.png)

## Can I filter which events I subscribe to?   [Skip link to Can I filter which events I subscribe to?](https://docs.recall.ai/docs/bot-status-change-events\#can-i-filter-which-events-i-subscribe-to)

Currently, filtering events isn't supported. This means you will receive all bot status change events for the lifecycle of your bots. If you don't need to use certain bot status change events, you can simply return a `2xx` success status code.

## Why is my webhook endpoint disabled?   [Skip link to Why is my webhook endpoint disabled?](https://docs.recall.ai/docs/bot-status-change-events\#why-is-my-webhook-endpoint-disabled)

If all attempts to a specific endpoint fail for a period of 5 days, the endpoint will be disabled. The clock only starts after multiple deliveries failed within a 24 hour span, with at least 12 hours difference between the first and the last failure.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI