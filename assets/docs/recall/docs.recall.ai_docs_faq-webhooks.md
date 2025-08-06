---
url: "https://docs.recall.ai/docs/faq-webhooks"
title: "FAQs: Webhooks"
---

## 1\. How are webhooks retried?   [Skip link to 1. How are webhooks retried?](https://docs.recall.ai/docs/faq-webhooks\#1-how-are-webhooks-retried)

Bot status change webhooks are sent via Svix and follow [their retry schedule](https://docs.svix.com/retries#the-schedule):

> Each message is attempted based on the following schedule, where each period is started following the failure of the preceding attempt:
>
> - Immediately
> - 5 seconds
> - 5 minutes
> - 30 minutes
> - 2 hours
> - 5 hours
> - 10 hours
> - 10 hours (in addition to the previous)
>
> If an endpoint is removed or disabled delivery attempts to the endpoint will be disabled as well.
>
> For example, an attempt that fails three times before eventually succeeding will be delivered roughly 35 minutes and 5 seconds following the first attempt.

> ## 📘
>
> This retry schedule only applies to webhooks sent through svix, and does not include [Real-Time Webhook Endpoints](https://docs.recall.ai/docs/real-time-webhook-endpoints).

## 2\. Why was my endpoint automatically disabled?   [Skip link to 2. Why was my endpoint automatically disabled?](https://docs.recall.ai/docs/faq-webhooks\#2-why-was-my-endpoint-automatically-disabled)

If all webhooks sent to a particular endpoint fail for 5 days, the endpoint will be automatically disabled. Endpoints can be re-enabled in the [webhooks dashboard](https://api.recall.ai/dashboard/webhooks/).

![Re-enabling a webhook endpoint](https://files.readme.io/aa34cb6-CleanShot_2024-04-08_at_13.46.21.png)

Re-enabling a webhook endpoint

More details can be found in the [Svix documentation](https://docs.svix.com/retries#disabling-failing-endpoints).

## 3\. How do I filter webhooks for a specific bot?   [Skip link to 3. How do I filter webhooks for a specific bot?](https://docs.recall.ai/docs/faq-webhooks\#3-how-do-i-filter-webhooks-for-a-specific-bot)

While the Webhook Message Viewer doesn't currently support filtering by specific bot statuses like "done", you can filter messages for a particular bot using the tag system. This method allows you to view all status change events for a specific bot.

Steps to Filter Messages by Bot ID:

**Open the Webhooks tab in the [Recall dashboard](https://recall.ai/login).**

**Locate the filter or tag input field:**

![](https://files.readme.io/89415d7285671cae3d2618b4e552ad42a72ac9cd1612a3626863cdc7df1e5dc3-CleanShot_2025-03-17_at_15.18.34.png)

**Enter the tag in the following format: `bot.id-{BOT_ID}`**

_Example: `bot.id-8ef3d462-bdcd-44dc-9d5a-af244449a209`_

Apply the filter and this will display all webhook events for the specified bot.

## 4\. What IP addresses are webhooks sent from?   [Skip link to 4. What IP addresses are webhooks sent from?](https://docs.recall.ai/docs/faq-webhooks\#4-what-ip-addresses-are-webhooks-sent-from)

You may want to whitelist IP addresses for webhook delivery depending on your security requirements.

A list of IP addresses to whitelist can be found in the Svix's documentation here: [Static source IP Addresses (EU)](https://docs.svix.com/receiving/source-ips#eu)

> ## 📘
>
> The above whitelist does not apply to data delivered through [Real-Time Endpoints](https://docs.recall.ai/docs/real-time-endpoints), which are not sent from static IP's.

Updated 12 days ago

* * *

Did this page help you?

Yes

No

Ask AI