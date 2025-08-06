---
url: "https://docs.recall.ai/docs/bot-overview"
title: "Bot Overview"
---

# What is a bot?   [Skip link to What is a bot?](https://docs.recall.ai/docs/bot-overview\#what-is-a-bot)

A **bot** is the fundamental entity for accessing a given meeting's data.

Bots are single-use, and are sent to meetings either ad-hoc ("on-the-fly"), or through scheduling them for a specific time.

Through a bot, you can interface with a meeting's video, audio, participants, and metadata in real-time during a call, as well as after the call for as long as the data is [retained](https://docs.recall.ai/docs/data-retention).

Whether you want to run real-time analysis, transcribe and record meetings, or extract summaries and intelligence using AI, this can all be done through a bot.

# Creating and scheduling bots   [Skip link to Creating and scheduling bots](https://docs.recall.ai/docs/bot-overview\#creating-and-scheduling-bots)

_How do I actually get bots to my meetings?_

There are two types of bots:

- **Ad-hoc bots:** These are on-demand bots, sent immediately to a meeting by making a [Create Bot](https://docs.recall.ai/reference/bot_create) request without specifying a `join_at` time.
- **Scheduled bots:** Bots can also be scheduled through the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint with a `join_at` parameter to specify when the bot should join a call.

> ## 📘  Scheduling bots to users' calendars
>
> Recall's [Calendar Integration](https://docs.recall.ai/docs/calendar-integration) is a layer on top of scheduled bots, allowing you to connect directly with user's calendars to automate the scheduling of bots to their calendar events.

# Video and Audio   [Skip link to Video and Audio](https://docs.recall.ai/docs/bot-overview\#video-and-audio)

Recall bots generate a recording that can be accessed in the `media_shortcuts` field of the bot when fetched from [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) or [List Bots](https://docs.recall.ai/reference/bot_list). The field will contain a pre-signed S3 URL that you can use to display the video in your application. Read more about this in our [Video Playback Guide](https://docs.recall.ai/docs/storage-and-playback#video-playback).

For real-time applications, you can leverage websockets for accessing raw video and audio streams in [real-time](https://docs.recall.ai/docs/real-time-audio-protocol)

# Transcription   [Skip link to Transcription](https://docs.recall.ai/docs/bot-overview\#transcription)

There are two ways to generate transcripts through Recall:

- **[Meeting Caption Transcription](https://docs.recall.ai/docs/meeting-caption-transcription):** Using the meeting platform's native closed captioning feature to generate a transcript in real-time.
- **[AI Transcription](https://docs.recall.ai/docs/ai-transcription):** Using a 3rd party AI transcription integration.

Which of these you choose depends on your requirements, and we recommend reviewing the documentation for each to decide which best fits your use case.

# Customizing your bots   [Skip link to Customizing your bots](https://docs.recall.ai/docs/bot-overview\#customizing-your-bots)

Recall bots are fully white label-able to match your branding:

- **[Output an Image](https://docs.recall.ai/docs/output-video-in-meetings):** Configure your bots to output a custom image.
- **Set the name for your bots:** Change the name of your bots by providing a `bot_name` parameter in the [Create Bot](https://docs.recall.ai/reference/bot_create) request.

Updated 21 days ago

* * *

Did this page help you?

Yes

No

Ask AI