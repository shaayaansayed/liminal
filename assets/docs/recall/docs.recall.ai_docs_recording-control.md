---
url: "https://docs.recall.ai/docs/recording-control"
title: "Recording Control"
---

Some use cases require having more granular control over when a bot records.

To support use cases that require more granular control over when a bot records, Recall provides 2 mechanisms:

1. **Pause/Resume Recording**
2. **Start/Stop Recording**

> ## 📘  Real-time transcription and recording
>
> When a bot isn't recording (is paused or stopped), real-time transcription will also be halted until recording begins again.

# Pause & Resume Recording   [Skip link to Pause & Resume Recording](https://docs.recall.ai/docs/recording-control\#pause--resume-recording)

* * *

> ## 📘
>
> The pause and resume recording endpoints allow you to control when a bot is recording, while still generating a _single_ recording.
>
> These endpoints are the recommended approach for generating a continuous recording of separate segments of a meeting.

[Pause Recording](https://docs.recall.ai/reference/bot_pause_recording_create) pauses the current recording.

[Resume Recording](https://docs.recall.ai/reference/bot_resume_recording_create) resumes the _same_ recording.

The result is a single recording file containing video/audio only from segments where the bot was not paused.

## FAQs   [Skip link to FAQs](https://docs.recall.ai/docs/recording-control\#faqs)

### Why is there a silent black screen in my recording?   [Skip link to Why is there a silent black screen in my recording?](https://docs.recall.ai/docs/recording-control\#why-is-there-a-silent-black-screen-in-my-recording)

This is the time the video was paused and the bot did not record the meeting.

### When I pause and then resume the recording, how does the transcript timestamp correlate to the recorded video?   [Skip link to When I pause and then resume the recording, how does the transcript timestamp correlate to the recorded video?](https://docs.recall.ai/docs/recording-control\#when-i-pause-and-then-resume-the-recording-how-does-the-transcript-timestamp-correlate-to-the-recorded-video)

The timestamps in the transcript align with the recorded video, which includes the black screen time. If you remove the black screen clip from the recording, you will also need to offset the transcript timestamps too

# Start & Stop Recording   [Skip link to Start & Stop Recording](https://docs.recall.ai/docs/recording-control\#start--stop-recording)

* * *

[Start Recording](https://docs.recall.ai/reference/bot_start_recording_create) triggers the bot to start recording. If a bot is already recording when this endpoint is called, a _new_ recording will begin, overwriting the old recording.

[Stop Recording](https://docs.recall.ai/reference/bot_stop_recording_create) stops the current recording of the bot and creates a new recording entry in the `recordings` field of the [bot](https://docs.recall.ai/reference/bot_retrieve).

> ## 📘  Accessing individual recordings
>
> In the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) response, the `recordings` field will contain the separate recordings, and you can access the corresponding video for each in the `media_shortcuts.video_mixed.data.download_url` field.
>
> For a single, contiguous recording of multiple recording segments, you should use [Pause & Resume Recording](https://docs.recall.ai/docs/recording-control#pauseresume-recording) .

# Manual Recording Control   [Skip link to Manual Recording Control](https://docs.recall.ai/docs/recording-control\#manual-recording-control)

* * *

If you don't want the bot to start recording when it joins a meeting, and want complete control over when it starts recording, you can add `recording_config: null` to your Create Bot configuration. At any point during the call, you can use the [Start Recording](https://docs.recall.ai/reference/bot_start_recording_create) endpoint to cause the bot to start producing a recording.

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI