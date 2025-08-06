---
url: "https://docs.recall.ai/docs/status-change-webhooks-setup-verification"
title: "Status Change Webhooks: Setup & Verification"
---

# Setup   [Skip link to Setup](https://docs.recall.ai/docs/status-change-webhooks-setup-verification\#setup)

Webhook endpoints are configured in the Recall dashboard in the "Webhooks" tab.

![](https://files.readme.io/9d2f436-Screen_Shot_2023-03-23_at_8.09.28_PM.png)

Click the "Add Endpoint" button on the right.

![](https://files.readme.io/76dc546-Screen_Shot_2023-03-23_at_8.35.07_PM.png)

Enter a URL from your application that Recall will call for event notifications, then click "Create".

![](https://files.readme.io/fd86ade-Screen_Shot_2023-03-23_at_8.38.50_PM.png)

Recall will submit a POST request to the configured URL, which your application can treat the same as any other route.

## Setting up a Test Endpoint   [Skip link to Setting up a Test Endpoint](https://docs.recall.ai/docs/status-change-webhooks-setup-verification\#setting-up-a-test-endpoint)

You can click the "Svix Play" button to generate a testing endpoint URL that will display all webhooks received.

![](https://files.readme.io/d53f346-Screen_Shot_2023-03-23_at_8.31.25_PM.png)

After clicking the "Create" button, you can view the webhooks sent to that URL by clicking "View in Svix Play".

![](https://files.readme.io/c39b4c0-Screen_Shot_2023-03-23_at_8.53.06_PM.png)

You will be taken to a page where you can view incoming webhook messages.

![](https://files.readme.io/588b070-Screen_Shot_2023-03-23_at_8.55.47_PM.png)

# Verification   [Skip link to Verification](https://docs.recall.ai/docs/status-change-webhooks-setup-verification\#verification)

The bot status webhooks (configured on [this page](https://api.recall.ai/dashboard/webhooks/)) are sent by Svix, and you can verify them as follows: [https://docs.svix.com/receiving/verifying-payloads/how-manual](https://docs.svix.com/receiving/verifying-payloads/how-manual)

Updatedover 1 year ago

* * *

Did this page help you?

Yes

No

Ask AI