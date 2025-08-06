---
url: "https://docs.recall.ai/reference/calendar_events_bot_create"
title: "Schedule Bot For Calendar Event"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

**For more information, see [Calendar V2](https://docs.recall.ai/docs/v2).**

> ## 📘  Override behavior
>
> When calling this endpoint for an event that already has a bot scheduled, the existing bot configuration will be overridden with the new settings provided in the request.

> ## 🚧  Meeting URL response shape
>
> Meeting URL's are currently improperly reflected in the API spec for **meeting URL's in responses**. For proper meeting URL shapes in API responses, please see [Meeting URL's](https://docs.recall.ai/docs/meeting-urls).
>
> `meeting_url`'s that are provided as a **parameter** to the API are reflected accurately in the API spec as strings.

### Scheduling error response   [Skip link to Scheduling error response](https://docs.recall.ai/reference/calendar_events_bot_create\#scheduling-error-response)

If you try to schedule a bot for an event that has already ended, you'll receive a 400 response:

JSON

```rdmd-code lang-json theme-light

{
  "code": "invalid_request_data",
  "message": "Unable to process request because invalid data was submitted. Check `errors` field for more details.",
  "errors": {
    "non_field_errors": [\
      "Cannot schedule bot as calendar event has ended."\
    ]
  }
}

```

id

uuid

required

A UUID string identifying this calendar event.

deduplication\_key

string

required

length ≤ 2000

Pass this key to deduplicate bots across multiple calendar events. Please ensure this remain consistent across all calendar events that mush share a single bot. For more details, refer to Calendar V2 scheduling guide.

bot\_config

object

required

The config object(JSON) to be passed to the bot. It supports all properties available in **[Create Bot request.](https://docs.recall.ai/reference/bot_create)**

`meeting_url` \- automatically populated from the calendar event unless specified in bot\_config.

`join_at` \- automatically populated from the calendar event

bot\_config object

# `` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v2/calendar-events/{id}/bot/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v2/calendar-events/id/bot/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 2 months ago

* * *

Did this page help you?

Yes

No