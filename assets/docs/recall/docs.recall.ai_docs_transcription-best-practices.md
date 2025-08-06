---
url: "https://docs.recall.ai/docs/transcription-best-practices"
title: "Transcription Best Practices"
---

There are a few common issues you can run into when enabling transcription for your meeting bots. Below are some common transcription questions along with answers and resources to go deeper:

# Q: How do I improve transcription quality?   [Skip link to Q: How do I improve transcription quality?](https://docs.recall.ai/docs/transcription-best-practices\#q-how-do-i-improve-transcription-quality)

Recall does not have direct control over the quality of the transcript. All transcripts are provided either by a 3rd party transcription provider, or by the native captions function of the meeting platform itself. However, you do still have configuration options available to you to improve the quality of the transcript.

### Use a different transcription model   [Skip link to Use a different transcription model](https://docs.recall.ai/docs/transcription-best-practices\#use-a-different-transcription-model)

There are two types of transcription model: real-time and asynchronous. Asynchronous transcription is typically higher quality than real-time transcription since the model gets the full context of the conversation when creating the transcription. If you’re okay with waiting until the end of the meeting to receive the transcript, you might want to look into using async transcription. Most of our supported transcription providers have both async and real-time models.

> ## 📘  Real-time vs. async in the Recall API
>
> To transcribe a meeting using asynchronous transcription, you need to call the [Create Transcript](https://docs.recall.ai/reference/recording_create_transcript_create) endpoint. If you’re setting up transcription in your [Create Bot](https://docs.recall.ai/reference/bot_create) request, it means you’re using a real-time transcription model instead of an async transcription model.

Related resources:

[Async Transcription](https://docs.recall.ai/docs/asynchronous-transcription) \| [Real-Time Transcription](https://docs.recall.ai/docs/real-time-transcription)

### Change your language configuration   [Skip link to Change your language configuration](https://docs.recall.ai/docs/transcription-best-practices\#change-your-language-configuration)

If you don’t know ahead of time which language the conversation will be in, you can set up automatic language detection. This is supported by most of the third-party transcription providers that we integrate with. Automatic language detection is not available when using meeting captions.

There are also cases where people switch back and forth between multiple languages in the same conversation. Some transcription providers also support this in their configuration options.

Related resources:

[Automatic Language Detection](https://docs.recall.ai/docs/real-time-transcription#languages)

### Add custom configuration based on your use case   [Skip link to Add custom configuration based on your use case](https://docs.recall.ai/docs/transcription-best-practices\#add-custom-configuration-based-on-your-use-case)

It’s worth investigating the different parameters available to you through the different providers. For example, if the transcript is consistently misspelling a company name or a certain proper noun, many transcription providers offer a “custom vocabulary” feature that allows you to specify the correct spelling. You can view all the supported parameters for the different transcription providers in our API Reference pages for [Create Bot](https://docs.recall.ai/reference/bot_create) and [Create Transcript](https://docs.recall.ai/reference/recording_create_transcript_create). You can also browse the documentation of your chosen transcription provider directly.

Related resources:

[Assembly AI](https://www.assemblyai.com/docs) \| [AWS Transcribe](https://docs.aws.amazon.com/transcribe/) \| [Deepgram](https://developers.deepgram.com/home/introduction) \| [Rev](https://docs.rev.ai/) \| [Speechmatics](https://docs.speechmatics.com/introduction)

# Q: How do I improve diarization quality?   [Skip link to Q: How do I improve diarization quality?](https://docs.recall.ai/docs/transcription-best-practices\#q-how-do-i-improve-diarization-quality)

Recall’s default diarization method is speaker timeline diarization, which uses the active speaker events from the meeting platform to assign names to speakers. This is generally accurate, but can run into issues when people interrupt each other or speak at the same time. Here are some options you can try if the default diarization isn't working for you:

### Use perfect diarization   [Skip link to Use perfect diarization](https://docs.recall.ai/docs/transcription-best-practices\#use-perfect-diarization)

Perfect diarization transcribes the audio streams of each meeting participant separately, which guarantees that words spoken by one person won’t be attributed to another. This is currently available for Zoom and Teams only.

Related resources:

[Perfect Diarization](https://docs.recall.ai/docs/perfect-diarization)

### Use machine diarization   [Skip link to Use machine diarization](https://docs.recall.ai/docs/transcription-best-practices\#use-machine-diarization)

Another alternative is machine diarization, which is available through the 3rd party transcription providers. This uses AI to recognize the sound of a speaker’s voice and assign words to them.

A primary use case for machine diarization is when you want to diarize words coming from a conference room where multiple people are talking as the same meeting participant. Speaker timeline diarization will think they’re all the same person, but machine diarization will recognize the individual speakers since it’s based on voice.

> ## 📘  Generic speaker labels
>
> Since the transcription provider doesn't have access to the names of the speakers in the meeting when it's doing diarization, the names of speakers will be generic labels like 0, 1, etc.

Related resources:

[Machine Diarization](https://docs.recall.ai/docs/diarization#machine-diarization)

# Q: How do I know which provider / configuration is the best?   [Skip link to Q: How do I know which provider / configuration is the best?](https://docs.recall.ai/docs/transcription-best-practices\#q-how-do-i-know-which-provider--configuration-is-the-best)

Each transcription provider has unique strengths and drawbacks, so the “best” transcription provider will likely look different depending on your use case.

We recommend picking out a few of the transcription providers and transcribing the exact same meeting multiple times using different providers and configurations. This will allow you to do a direct comparison of the transcript quality for the same conversation. You can do this by recording a conversation, and then calling the Analyze Bot Media endpoint to transcribe it. Save the resulting transcript, then run Analyze Bot Media again using a different provider or configuration. This should help you understand what works best for your unique use case.

Updated6 days ago

* * *

Did this page help you?

Yes

No

Ask AI