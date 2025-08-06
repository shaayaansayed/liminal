---
url: "https://docs.recall.ai/docs/speaker-timeline"
title: "Speaker Timelines"
---

A speaker timeline is a history of active speaker events for a bot.

Recall uses this timeline for transcript [diarization](https://docs.recall.ai/docs/diarization), and also exposes it through the Participant Events resource associated with the recording.

## Timestamps   [Skip link to Timestamps](https://docs.recall.ai/docs/speaker-timeline\#timestamps)

The timestamp for each active speaker events is offset in seconds relative to the bot's `in_call_recording` event.

## Fetching the speaker timeline   [Skip link to Fetching the speaker timeline](https://docs.recall.ai/docs/speaker-timeline\#fetching-the-speaker-timeline)

After calling [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve), you can download a speaker timeline from the `media_shortcuts.participant_events.data.speaker_timeline_download_url` field in the `recordings` object(s). View the response format [response format here](https://docs.recall.ai/docs/download-schemas#json-speaker-timeline-download-url).

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI