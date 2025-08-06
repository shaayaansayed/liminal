---
url: "https://docs.recall.ai/docs/webex"
title: "Webex Overview"
---

> ## 🛠️  Setup required
>
> Webex bots are not supported "out-of-the-box" and require some initial setup.
>
> To start sending bots to Webex calls, follow the [Webex Bot Setup](https://docs.recall.ai/docs/webex-bot-setup) guide.

# Limitations   [Skip link to Limitations](https://docs.recall.ai/docs/webex\#limitations)

* * *

Before getting started with Webex bots, there are some important limitations to be aware of.

## Active speaker events   [Skip link to Active speaker events](https://docs.recall.ai/docs/webex\#active-speaker-events)

Active speaker events will only be available if the meeting host:

- Is on a **paid** Webex account
- Has closed captions turned **on** for the meeting

## Audio limitations   [Skip link to Audio limitations](https://docs.recall.ai/docs/webex\#audio-limitations)

Webex only supports a single, combined stream of audio.

`automatic_audio_output` in [Create Bot](https://docs.recall.ai/reference/bot_create) is not supported.

## Video limitations   [Skip link to Video limitations](https://docs.recall.ai/docs/webex\#video-limitations)

Webex only supports one combined video stream with no support for layout configuration.

The current behavior is video of the active speaker in the call (prominent) + up to 6 other video participants (in footer tray).

## Caption limitations   [Skip link to Caption limitations](https://docs.recall.ai/docs/webex\#caption-limitations)

Captions through Webex's native transcription service are currently not supported. To transcribe a conversation in real-time on a Webex meeting, you'll need to use one of the [AI Transcription Providers](https://docs.recall.ai/docs/ai-transcription#ai-transcription-providers).

Updated 3 months ago

* * *

Did this page help you?

Yes

No

Ask AI