---
url: "https://docs.recall.ai/docs/meeting-metadata"
title: "Meeting Metadata"
---

Recall.ai exposes metadata for a given meeting as media object on a recording.

Examples of meeting metadata include meeting title and unique identifiers, though the specific metadata available depends on the platform.

# Configuration   [Skip link to Configuration](https://docs.recall.ai/docs/meeting-metadata\#configuration)

To configure a bot to record meeting metadata, provide a `meeting_metadata` object in your [Create Bot](https://docs.recall.ai/reference/bot_create) request's `recording_config`:

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "meeting_url": "https://meet.google.com/gtt-vjsi-jhj",
  "recording_config": {
    "meeting_metadata": {}
  }
}
'

```

# Retrieving Meeting Metadata   [Skip link to Retrieving Meeting Metadata](https://docs.recall.ai/docs/meeting-metadata\#retrieving-meeting-metadata)

**Platform Support**

| Platform | Supported? |  |
| --- | --- | --- |
| Zoom | ✅ |  |
| Google Meet | ⚠️ | Only works if:<br>\- Bot is signed<br>\- Bot is a participant on the calendar event<br>\- Calendar event's end time is in the future |
| Microsoft Teams | ❌ |  |
| Cisco Webex | ❌ |  |
| Slack Huddles | ✅ |  |

To retrieve meeting metadata for a recording, you can either:

- Call [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) and access the metadata in `shortcuts.meeting_metadata.data` in the recording object
- Call [Retrieve Meeting Metadata](https://docs.recall.ai/reference/meeting_metadata_retrieve), using the ID of the meeting metadata artifact
- Call [List Meeting Metadata](https://docs.recall.ai/reference/meeting_metadata_list), filtering to a specific recording ID

### Google Meets   [Skip link to Google Meets](https://docs.recall.ai/docs/meeting-metadata\#google-meets)

The Microsoft Teams title will only be populated if the bot is signed in and the bots email on the calendar meeting invite

JSON

```rdmd-code lang-json theme-light

{
  "data": {
      "title": "John Smith's Personal Meeting Room",
    },
  },
  ...
}

```

### Zoom   [Skip link to Zoom](https://docs.recall.ai/docs/meeting-metadata\#zoom)

JSON

```rdmd-code lang-json theme-light

{
  "data": {
      "title": "John Smith's Personal Meeting Room",
      "zoom_meeting_uuid": "x7OAB2GkQmFZuNhAY+nTNg=="
    },
  },
  ...
}

```

### Slack Huddles   [Skip link to Slack Huddles](https://docs.recall.ai/docs/meeting-metadata\#slack-huddles)

JSON

```rdmd-code lang-json theme-light

{
  "data": {
      "huddle_id": "...",
      "channel_id": "..."
    },
  },
  ...
}

```

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI