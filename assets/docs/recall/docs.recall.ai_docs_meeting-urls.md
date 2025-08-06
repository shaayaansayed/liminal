---
url: "https://docs.recall.ai/docs/meeting-urls"
title: "Meeting URL's"
---

> ## 🚧  API Reference under construction
>
> We're working on fixing how `meeting_url` is documented in our API reference. In the meantime, here is a reference for the shapes of various platform meeting URL's.

## Zoom   [Skip link to Zoom](https://docs.recall.ai/docs/meeting-urls\#zoom)

```rdmd-code lang- theme-light
"meeting_url": {
  "meeting_id": string,
  "meeting_password": string | null,
  "platform": "zoom"
}

```

## Google Meet   [Skip link to Google Meet](https://docs.recall.ai/docs/meeting-urls\#google-meet)

```rdmd-code lang- theme-light
"meeting_url": {
  "meeting_id": string,
  "platform": "google_meet"
}

```

## Microsoft Teams   [Skip link to Microsoft Teams](https://docs.recall.ai/docs/meeting-urls\#microsoft-teams)

```rdmd-code lang- theme-light
"meeting_url": {
  "meeting_id": string | null,
  "meeting_password": string | null,
  "organizer_id": string | null,
  "tenant_id": string | null,
  "message_id": string | null,
  "thread_id": string | null,
  "business_meeting_id": string | null,
  "business_meeting_password": string | null,
  "platform": "microsoft_teams" | "microsoft_teams_live"
}

```

> ## 📘  Microsoft Teams URL differences
>
> Microsoft Teams meeting URL use different parameters depending on the Teams version being used.
>
> The table below shows what you can expect for each Teams version meeting URL.
>
> | Version | Base URL | Non-null Parameters |
> | --- | --- | --- |
> | Teams for Business | `teams.microsoft.com` | `organizer_id`<br>`tenant_id`<br>`message_id`<br>`thread_id` |
> | Teams for Personal use | `teams.live.com` | `meeting_id`<br>`meeting_password` |

## Webex   [Skip link to Webex](https://docs.recall.ai/docs/meeting-urls\#webex)

```rdmd-code lang- theme-light
"meeting_url": {
  "meeting_subdomain": string,
  "meeting_mtid": string,
  "meeting_path": string,
  "platform": "webex"
}

```

## GoTo   [Skip link to GoTo](https://docs.recall.ai/docs/meeting-urls\#goto)

```rdmd-code lang- theme-light
  "meeting_url": {
    "meeting_id": "680504437",
    "platform": "goto_meeting"
  }

```

Updated 8 months ago

* * *

Did this page help you?

Yes

No

Ask AI