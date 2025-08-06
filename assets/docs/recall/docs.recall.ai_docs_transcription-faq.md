---
url: "https://docs.recall.ai/docs/transcription-faq"
title: "Transcription FAQ"
---

## How do I match words with calendar participants or email addresses?   [Skip link to How do I match words with calendar participants or email addresses?](https://docs.recall.ai/docs/transcription-faq\#how-do-i-match-words-with-calendar-participants-or-email-addresses)

You may find yourself wanting to match speakers from the transcription to calendar participants or email addresses.

Unfortunately there isn't a direct way to match speakers from transcriptions to calendar participants since meeting platforms don't expose participant emails for privacy reasons.

A common workaround is to get emails via the calendar integration and do a fuzzy match on a bot's meeting participant names to associate them with emails. This isn't perfect, but can work well enough depending on your use case.

## Why is the speaker "None" at the start of a transcript?   [Skip link to Why is the speaker "None" at the start of a transcript?](https://docs.recall.ai/docs/transcription-faq\#why-is-the-speaker-none-at-the-start-of-a-transcript)

At the start of a call, someone may be already speaking prior to the bot joining. In this case, there is no active speaker event to tie to the first utterance in the transcript.

In this case, the first utterance will have a speaker of `null`.

## How do I determine transcription hours for a given bot?   [Skip link to How do I determine transcription hours for a given bot?](https://docs.recall.ai/docs/transcription-faq\#how-do-i-determine-transcription-hours-for-a-given-bot)

The recommended approach here is to use the `recordings` field on the bot object.

This will contain an object (or multiple objects if the bot was started and stopped during the call), with `started_at` and `completed_at` timestamps you can use to calculate the recording time. Since the whole recording is sent to the transcription provider, this will be equivalent to the transcription time for the bot.

**Example `recordings`**:

JSON

```rdmd-code lang-json theme-light

"recordings": [\
  {\
    "id": "b3181d8e-05fb-42c0-940a-c9607d7da7ff",\
    "started_at": "2024-02-02T22:05:51.232821Z",\
    "completed_at": "2024-02-02T22:07:00.691048Z"\
  }\
]

```

## Fetching custom fields from your transcription provider   [Skip link to Fetching custom fields from your transcription provider](https://docs.recall.ai/docs/transcription-faq\#fetching-custom-fields-from-your-transcription-provider)

If you want to extract a specific field from your transcription provider that is not exposed through the Recall API, then you can download the raw provider data from the [transcript artifact](https://docs.recall.ai/reference/transcript_retrieve):

json

```rdmd-code lang-json theme-light

{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "data": {
    "provider_data_download_url": "..."
  }
}

```

Then download the data from `data.provider_data_download_url` extract the specific field you need. See the [response format here](https://docs.recall.ai/docs/download-schemas#json-transcript-provider-data-download-url).

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI