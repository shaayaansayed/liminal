---
url: "https://docs.recall.ai/docs/recording-webhooks"
title: "Recording Webhooks"
---

## Recording Status Webhook   [Skip link to Recording Status Webhook](https://docs.recall.ai/docs/recording-webhooks\#recording-status-webhook)

This webhook is sent whenever the recording's status is changed and is delivered via Svix to the endpoints configured in your [Recall dashboard](https://api.recall.ai/dashboard/webhooks/).

JSON

```rdmd-code lang-json theme-light

{
  "event": "recording.processing", // recording.done, recording.failed, recording.deleted
  "data": {
    "data": {
      "code": string,
      "sub_code": string | null,
      "updated_at": string
    },
    "recording": {
      "id": string,
      "metadata": object
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
| `recording.processing` | The recording has started |
| `recording.done` | The recording has successfully completed. All data for media objects on the recording is now available |
| `recording.failed` | The recording failed to be captured. The `data.sub_code` will contain machine readable code for the failure |
| `recording.deleted` | The recording has been deleted from Recall systems. |

## Media Object Status Webhook   [Skip link to Media Object Status Webhook](https://docs.recall.ai/docs/recording-webhooks\#media-object-status-webhook)

This webhook is sent whenever the media object's status is changed and is delivered via Svix to the endpoints configured in your [Recall dashboard](https://api.recall.ai/dashboard/webhooks/). The following media object are supported

- `participant_events`
- `transcript`
- `video_mixed`
- `video_separate`
- `audio_mixed`
- `audio_separate`
- `meeting_metadata`

Example structure:

JSON

```rdmd-code lang-json theme-light

{
  "event": "participant_events.processing",
  "data": {
    "data": {
      "code": string,
      "sub_code": string | null,
      "updated_at": string
    },
    "participant_events": {
      "id": string,
      "metadata": object,
    },
    "recording": {
      "id": string,
      "metadata": object
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
| `participant_events.processing` | The media object has started capturing |
| `participant_events.done` | The media object has successfully completed. All data for media objects on the recording is now available |
| `participant_events.failed` | The media object failed to be captured. The `data.sub_code` will contain machine readable code for the failure |
| `participant_events.deleted` | The media object has been deleted from Recall systems. |

## Transcript Status Webhooks   [Skip link to Transcript Status Webhooks](https://docs.recall.ai/docs/recording-webhooks\#transcript-status-webhooks)

JSON

```rdmd-code lang-json theme-light

{
  "event": "transcript.processing", // done, failed, deleted
  "data": {
    "data": {
      "code": string,
      "sub_code": string | null,
      "updated_at": string
    },
    "transcript": {
      "id": string,
      "metadata": object,
    },
    "recording": {
      "id": string,
      "metadata": object
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
| `transcript.processing` | The media object has started capturing |
| `transcript.done` | The media object has successfully completed. All data for media objects on the recording is now available |
| `transcript.failed` | The media object failed to be captured. The `data.sub_code` will contain machine readable code for the failure. See below for list of sub codes |
| `transcript.deleted` | The media object has been deleted from Recall systems. |

**Transcript Failure Sub Codes**

| Event | Sub Code | Reason |
| --- | --- | --- |
| `transcript.failed` | `provider_connection_failed` | Recall is not able to connect to the 3rd party transcription provider. Common reasons for these include:<br>\- Insufficient funds in the transcription provider account for which the API key is provided<br>\- Using paid features on a free account<br>\- Temporary service unavailability from the transcription provider |
| `transcript.failed` | `zoom_global_captions_disabled` | Meeting captions are disabled by the Zoom account |
| `transcript.failed` | `zoom_host_disabled_meeting_captions` | The host of Zoom meeting has disabled meeting captions |
| `transcript.failed` | `zoom_captions_failure` | There was an error in enabling meeting captions for the Zoom call |

Updated 27 days ago

* * *

Did this page help you?

Yes

No

Ask AI