---
url: "https://docs.recall.ai/docs/custom-metadata"
title: "Custom Metadata"
---

You can attach custom metadata to [Recordings](https://docs.recall.ai/docs/recordings-and-media), [Media](https://docs.recall.ai/docs/recordings-and-media#media), and data sources (such as [Bots](https://docs.recall.ai/docs/bot-overview)) through their corresponding `metadata` field.

Any attached metadata will be present on the corresponding resource when fetched through the API, which can be useful for maintaining relationships with internal data models, or tagging resources with specific pieces of information.

**Example: Tag a Bot's Recording with an internal user ID:**

```rdmd-code lang- theme-light
curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header 'Authorization: $RECALLAI_API_KEY' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "recording_config": {
    "metadata": {
      "user_id": "12345"
    }
  }
}
'

```

The `metadata` will be available through the recording's `metadata` field (for instance, when calling [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve).

It will also be present when receiving a corresponding webhook. For instance, a Recording status change webhook:

```rdmd-code lang- theme-light
{
  "event": "recording.done",
  "data": {
    "recording": {
      "id": string,
      "metadata": {
        "user_id": "12345"
      }
    },
    ...
  }
}

```

> ## ⚠️  Field Limitations
>
> Each value in a custom metadata key-value pair has a maximum length of **500 characters**.

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI