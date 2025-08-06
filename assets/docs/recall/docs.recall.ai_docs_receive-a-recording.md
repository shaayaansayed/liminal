---
url: "https://docs.recall.ai/docs/receive-a-recording"
title: "Bot Recording"
---

# Configure a bot to record an mp4   [Skip link to Configure a bot to record an mp4](https://docs.recall.ai/docs/receive-a-recording\#configure-a-bot-to-record-an-mp4)

When calling [Create Bot](https://docs.recall.ai/reference/bot_create), you can configure a bot to generate a recording artifact by specifying this in the `recording_config` object:

cURL

```rdmd-code lang-curl theme-light

curl -X POST "https://us-east-1.recall.ai/api/v1/bot/" \
     -H "Authorization: $RECALLAI_API_KEY" \
     -H "accept: application/json" \
     -H "content-type: application/json" \
     -d '
{
  "meeting_url": "https://meet.google.com/pdh-dwvu-cqn",
  "recording_config": {
    "video_mixed_mp4": {}
  }
}
'

```

# Fetch a recording   [Skip link to Fetch a recording](https://docs.recall.ai/docs/receive-a-recording\#fetch-a-recording)

Once the bot's call has completed, you'll receive a `done` [Bot Status Change Webhook](https://docs.recall.ai/docs/status-change-webhooks-setup-verification), upon which you can call the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) endpoint:

cURL

```rdmd-code lang-curl theme-light

curl -X GET "https://us-east-1.recall.ai/api/v1/bot/{BOT_ID}/" \
     -H "Authorization: $RECALLAI_API_KEY" \
     -H "accept: application/json"

```

In the response, the `recordings` field will be populated a recording object (or multiple if using the [Stop Recording](https://docs.recall.ai/reference/bot_stop_recording_create) & [Start Recording](https://docs.recall.ai/reference/bot_start_recording_create) endpoints).

The `media_shortcuts` field will have shortcuts to recording media objects, including the `video_mixed`. The `data.download_url` on this to will contain a pre-signed S3 link to download the recording.

JSON

```rdmd-code lang-json theme-light

{
  "id": "6e1f5adb-3340-4f50-900d-9aa2cdc53d6c",
  "recordings": [\
    {\
      "id": "5a7062f3-bd54-4838-b296-df84f85c7b92",\
      "created_at": "2024-12-03T02:54:11.397104Z",\
      "started_at": "2024-12-03T02:54:43.157376Z",\
      "completed_at": "2024-12-03T02:55:03.088727Z",\
      "expires_at": "2024-12-10T02:55:03.088727Z",\
      "bot": {\
        "id": "6e1f5adb-3340-4f50-900d-9aa2cdc53d6c",\
        "metadata": {}\
      },\
      "status": {\
        "code": "done",\
        "sub_code": null,\
        "updated_at": "2024-12-03T02:55:03.088727Z"\
      },\
      "media_shortcuts": {\
        "video_mixed": {\
          "id": "04530d90-6745-455a-b190-e55d463cbb2a",\
          "recording_id": "5a7062f3-bd54-4838-b296-df84f85c7b92",\
          "created_at": "2024-12-03T02:54:43.157376Z",\
          "expires_at": "2024-12-10T02:55:03.088727Z",\
          "status": {\
            "code": "done",\
            "sub_code": null,\
            "updated_at": "2024-12-03T02:55:03.088727Z"\
          },\
          "metadata": {},\
          "data": {\
            "download_url": "https://recallai-production-bot-data.s3.amazonaws.com/..."\
          },\
          "format": "mp4"\
        },\
      }\
    }\
  ]
}

```

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI