---
url: "https://docs.recall.ai/docs/zoom-email-required-meetings"
title: "Email Required Meetings"
---

Certain Zoom meetings and webinars require an email in order to join.

If a Zoom bot attempts to join one of these calls and isn't configured with an email, it will produce a `fatal` error with the following sub code: `zoom_email_required`.

## Configuring an email   [Skip link to Configuring an email](https://docs.recall.ai/docs/zoom-email-required-meetings\#configuring-an-email)

To enable bots to join email-required meetings and webinars, you can provide a `user_email` in the `zoom` configuration object of your [Create Bot](https://docs.recall.ai/reference/bot_create) request:

JSON

```rdmd-code lang-json theme-light

{
  "zoom": {
    "user_email": "john@email.com"
  },
}

```

If the meeting or webinar requires [registration](https://docs.recall.ai/docs/registration-required-meetings-webinars), this email does _not_ have to match the email of the user that registered. You can use any email address.

## Bot Support   [Skip link to Bot Support](https://docs.recall.ai/docs/zoom-email-required-meetings\#bot-support)

| Bot type | Supported? |
| --- | --- |
| Zoom Web (default) | ✅ |
| Zoom Native | ❌ |

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI