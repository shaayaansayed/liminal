---
url: "https://docs.recall.ai/docs/local-webhook-development"
title: "Local Webhook Development"
---

Before deploying webhook functionality to staging or production, you'll likely want to test it locally.

Since webhook signature verification can introduce unique challenges when trying to mock them (e.g. through Postman), this is the recommended approach for developing & testing webhooks on your local machine.

## Ngrok setup   [Skip link to Ngrok setup](https://docs.recall.ai/docs/local-webhook-development\#ngrok-setup)

[Create](https://dashboard.ngrok.com/) an ngrok account if you don't already have one.

Download the [Ngrok CLI](https://ngrok.com/download) and authenticate your account.

## Set up a static domain   [Skip link to Set up a static domain](https://docs.recall.ai/docs/local-webhook-development\#set-up-a-static-domain)

> ## 📘  Static vs ephemeral ngrok domains
>
> Ngrok tunnels to test webhooks locally can either use static or ephemeral domains.
>
> In order to be able to use the same webhook URL when testing, we **highly recommend** setting up and using a static domain. This will allow you to avoid reconfiguring the webhook dashboard, or updating your API calls to use a different endpoint every time you open a new tunnel.
>
> Free accounts can claim one static domain.

To set up a static ngrok domain:

1. Sign in to your ngrok account.
2. Navigate to [Cloud Edge > Domains](https://dashboard.ngrok.com/cloud-edge/domains).‍
3. Follow the prompts to claim your unique, static domain.

## Start a tunnel   [Skip link to Start a tunnel](https://docs.recall.ai/docs/local-webhook-development\#start-a-tunnel)

Now that you have a static domain you can use as your publicly exposed webhook URL, we need to open an ngrok tunnel to a local port.

This will enable us to receive webhook events sent to the public endpoint at a port locally.

To do this, run:

```rdmd-code lang- theme-light
ngrok http --domain {YOUR_STATIC_DOMAIN} {PORT}

```

For instance, if my static ngrok domain is `my-static-domain.ngrok-free.app` and I want to receive webhook events locally on port 8080, I can run:

```rdmd-code lang- theme-light
ngrok http --domain my-static-domain.ngrok-free.app 8080

```

**In your terminal, you should see something like this:**

Text

```rdmd-code lang-text theme-light

Session Status                online
Account                       johndoe (Plan: Free)
Version                       3.5.0
Region                        United States (us)
Latency                       -
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://my-static-domain.ngrok-free.app -> http://localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00

```

Now, any events sent to `my-static-domain.ngrok-free.app` will be forwarded to `localhost:8080`.

Updated over 1 year ago

* * *

- [Calendar V2 Webhooks](https://docs.recall.ai/docs/calendar-v2-webhooks)

Did this page help you?

Yes

No

Ask AI