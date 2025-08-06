---
url: "https://docs.recall.ai/docs/perfect-diarization"
title: "Perfect Diarization"
---

> ## 📘  Supported Platforms
>
> Perfect diarization is currently supported for Zoom Native and Teams Web bots.

Perfect diarization is a feature designed to address the problem of inaccurate speaker attribution in meeting transcripts. Meeting platforms can sometimes attribute words to the wrong speaker, especially when multiple people are talking at once. This feature ensures that each speaker's words are accurately identified, even when participants are talking over each other.

## How It Works   [Skip link to How It Works](https://docs.recall.ai/docs/perfect-diarization\#how-it-works)

Perfect diarization transcribes separate audio streams for each participant instead of using the combined audio stream for the entire meeting, significantly improving the accuracy of speaker attribution.

This feature is compatible with all [AI transcription providers](https://docs.recall.ai/docs/ai-transcription#ai-transcription-providers) supported by Recall.ai and can be used for [real-time transcription](https://docs.recall.ai/docs/real-time-transcription).

## Usage   [Skip link to Usage](https://docs.recall.ai/docs/perfect-diarization\#usage)

To configure perfect diarization in a [Create Bot](https://docs.recall.ai/reference/bot_create) request, set the `use_separate_streams_when_available` to `true` in your `recording_config.transcript.diarization` config:

JSON

```rdmd-code lang-json theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "recording_config": {
    "transcript": {
      "diarization": {
        "use_separate_streams_when_available": true
      },
      "provider": {
        ...
      }
    }
  }
}
'

```

## Important Considerations   [Skip link to Important Considerations](https://docs.recall.ai/docs/perfect-diarization\#important-considerations)

**Increased Transcription Usage:** Transcribing multiple streams may result in higher costs from your transcription provider. On average, usage is ~1.8x higher than single-stream transcription.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI