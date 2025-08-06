---
url: "https://docs.recall.ai/docs/storage-and-playback"
title: "Storage and Playback Overview"
---

Once you've started creating recordings and transcripts, you'll likely want to display them to your users.

# Video Playback   [Skip link to Video Playback](https://docs.recall.ai/docs/storage-and-playback\#video-playback)

The quickest way to display videos in your application is to stream recordings directly from Recall's S3 storage using the video URLs provided by Recall's API. This eliminates the need to download, store, and re-host large video files on your own infrastructure.

## Direct streaming   [Skip link to Direct streaming](https://docs.recall.ai/docs/storage-and-playback\#direct-streaming)

When you [retrieve a recording](https://docs.recall.ai/reference/recording_retrieve) using the API, the response will include a temporary S3 URL in the `media_shortcuts.video_mixed.data.download_url` field. These URLs point directly to the recorded content and can be used as video sources in your web application:

HTML

```rdmd-code lang-html theme-light

<video controls width="800" height="600">
  <source src="https://recallai-production-bot-data.s3.amazonaws.com/..." type="video/mp4">
</video>

```

## Handling URL expiration   [Skip link to Handling URL expiration](https://docs.recall.ai/docs/storage-and-playback\#handling-url-expiration)

The S3 URLs are signed and expire after 6 hours for security reasons. Rather than caching these URLs, you should fetch fresh ones each time a user needs to access a recording:

1. When a user requests to view a recording: Make an API call to retrieve the recording data
2. Extract the current `download_url` from the `media_shortcuts.video_mixed.data` field
3. Use this URL immediately as the video source in your HTML

This pattern ensures users always receive valid, non-expired URLs while keeping your application lightweight.

For a more detailed implementation, you can reference this [sample application](https://github.com/recallai/recording-viewer-demo).

# Storage Duration   [Skip link to Storage Duration](https://docs.recall.ai/docs/storage-and-playback\#storage-duration)

By default, all media associated with a recording is retained forever. This applies for all accounts created after June 12, 2025.

Recall supports specifying custom retention for the recordings captured by a bot via the `recording_config.retention` field in [Create Bot](https://docs.recall.ai/reference/bot_create) request. Two retention types are supported:

1. **Timed**


Allows you to specify a custom retention duration in hours via the required `hours` property (e.g., hours: 72 for 3 days). The recording will expire after the specified number of hours from creation.


```rdmd-code lang- theme-light
{
     "type": "timed",
     "hours": <NUMBER_OF_HOURS_TO_RETAIN>
}

```

2. **Forever**


The recording will never expire and will be retained indefinitely unless explicitly deleted.


```rdmd-code lang- theme-light
{
     "type": "forever"
}

```


## Pricing   [Skip link to Pricing](https://docs.recall.ai/docs/storage-and-playback\#pricing)

Recall provides 7 days of free recording retention. After that, additional retention is charged at:

> **$0.05 per hour of recording retained for 30 days**
>
> (Equivalent to $0.0000694 per hour of recording retained)

For e.g If you retain a 1-hour recording for 30 additional days, the total cost is:

`$0.0000694 × 1 recording hour × 720 hours (30 days) = $0.05`

If you have any questions regarding pricing, please reach out to us via [support@recall.ai](mailto:support@recall.ai) or through Slack for more information.

# Media Expiration   [Skip link to Media Expiration](https://docs.recall.ai/docs/storage-and-playback\#media-expiration)

Recording data can be deleted at any point by calling [Delete Bot Media](https://docs.recall.ai/reference/bot_delete_media_create) or [Delete Recording](https://docs.recall.ai/reference/recording_destroy). After data has been deleted, it is **permanently** removed from Recall servers and cannot be recovered.

> ## 📘
>
> Custom metadata and the meeting URL are not deleted upon media expiration/deletion for a bot.

## Recording Media   [Skip link to Recording Media](https://docs.recall.ai/docs/storage-and-playback\#recording-media)

**Media** refers to:

- Recording
- Transcript
- Speaker timeline
- Meeting URL
- Participant metadata (who joined, left, timestamps)
- Meeting metadata (e.g. Meeting title)
- Video files, audio files, and any other media
- Bot screenshots
- Debug data

_Note: Deleting bot media through the API does not delete logs. Log files will be automatically deleted after the 7 day retention period._

The media expiration date for a given recording can be found in the `expires_at` field of the [Recording](https://docs.recall.ai/reference/recording_retrieve):

```rdmd-code lang- theme-light
{
  "id": "a5437136-4b69-429a-9e0c-cd388fd8fee6",
  "expires_at": "2024-12-27T00:07:47.409813Z",
  ...
}

```

## The `recording.deleted` Webhook   [Skip link to The ](https://docs.recall.ai/docs/storage-and-playback\#the-recordingdeleted-webhook)

When a recording reaches its expiration date and is deleted, you will receive a `recording.deleted` [Status Change Webhook](https://docs.recall.ai/docs/status-change-webhooks-setup-verification) to notify you of this.

# Security   [Skip link to Security](https://docs.recall.ai/docs/storage-and-playback\#security)

## Zero Data Retention   [Skip link to Zero Data Retention](https://docs.recall.ai/docs/storage-and-playback\#zero-data-retention)

If you have strict data privacy concerns, you may want to ensure that no recording data is ever stored on Recall's servers at any point. You can accomplish this by setting the `recording_config.retention` field to be `null` in your [Create Bot](https://docs.recall.ai/reference/bot_create) request. This will ensure that no data is retained at any point.

When zero data retention is configured, the only way to access meeting data will be to stream it in real time while the meeting is occurring. Refer to our guides on streaming [audio](https://docs.recall.ai/reference/real-time-audio-protocol), [video](https://docs.recall.ai/reference/stream-real-time-video-rtmp), and [transcripts](https://docs.recall.ai/reference/real-time-transcription) for more information.

Note that retaining zero data will make debugging any issues or failures associated with the bot more difficult since no backup data is stored in Recall.

## Encryption   [Skip link to Encryption](https://docs.recall.ai/docs/storage-and-playback\#encryption)

Bot data is encrypted at rest in our database for additional security. For additional information on how data is secured, please visit our [security portal](https://security.recall.ai/).

Updated 6 days ago

* * *

Did this page help you?

Yes

No

Ask AI