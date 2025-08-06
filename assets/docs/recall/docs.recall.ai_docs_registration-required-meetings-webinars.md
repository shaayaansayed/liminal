---
url: "https://docs.recall.ai/docs/registration-required-meetings-webinars"
title: "Registration-Required Meetings & Webinars"
---

> ## 📘  Registration-required meetings & webinars are supported by **web bots** only.

Recall supports sending bots to registration-required Zoom meetings and webinars.

For a bot to join a registration-required meeting, there are two things required:

1. A `tk` parameter in the meeting URL
2. \*An email address

_\*For Zoom webinars, the bot **must** be added as a panelist._

## `tk` query parameter   [Skip link to [object Object]](https://docs.recall.ai/docs/registration-required-meetings-webinars\#tk-query-parameter)

Once a user registers for the meeting or webinar, they will receive a meeting URL from Zoom containing a `tk` query parameter.

When calling [Create Bot](https://docs.recall.ai/reference/bot_create), you should ensure that the `meeting_url` contains this.

## `user_email`   [Skip link to [object Object]](https://docs.recall.ai/docs/registration-required-meetings-webinars\#user_email)

If registration is required for a meeting or webinar, Zoom requires an email in the join request.

This should be provided in the `zoom.user_email` parameter in the [Create Bot](https://docs.recall.ai/reference/bot_create) request:

JSON

```rdmd-code lang-json theme-light

{
  "zoom": {
    "user_email": "john@email.com"
  },
}

```

> ## 📘
>
> This email does _not_ have to match the email that was registered for the event. For simplicity's sake, you can provide a hard-coded email address such as `bot@yourcompany.com`.
>
> This can be provided regardless of whether the meeting is a registration-required Zoom meeting or not.

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI