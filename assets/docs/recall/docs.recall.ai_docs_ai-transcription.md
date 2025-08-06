---
url: "https://docs.recall.ai/docs/ai-transcription"
title: "AI Transcription"
---

In addition to meeting caption transcriptions, Recall also integrates with several AI transcription partners as a solution for producing transcripts, as well as meeting intelligence such as summarization and sentiment analysis.

There are two options for transcription when using one of our AI transcription partners:

1. **[Real-time transcription](https://docs.recall.ai/docs/real-time-transcription)**: Transcript is generated in real-time.
2. **[Async Transcription](https://docs.recall.ai/docs/asynchronous-transcription)**: Transcript is generated after the call has completed.

Both methods have pros and cons, and which you choose will ultimately depend on your use case.

If you don't have a need for receiving transcripts in real-time, we recommend starting with asynchronous transcription, as it's generally more accurate and cost effective.

> ## ❗️  Important: Concurrency considerations
>
> When going to production, make sure that your account with your 3rd party transcription provider is configured with high enough concurrency limit to support your anticipated load.
>
> Certain transcription providers require that you reach out to increase your concurrency limit, and we highly recommend checking this prior to running production workloads.

# AI Transcription Providers   [Skip link to AI Transcription Providers](https://docs.recall.ai/docs/ai-transcription\#ai-transcription-providers)

To use a given transcription provider, you can add an API key for the provider in the Recall dashboard using their corresponding dashboard link.

| Provider | Provider Information | Regions |
| --- | --- | --- |
| Assembly AI | [AssemblyAI Pricing](https://www.assemblyai.com/pricing) | `api.assemblyai.com` |
| AWS Transcribe | [AWS Transcribe Pricing](https://aws.amazon.com/transcribe/pricing/) | Any supported AWS region |
| Deepgram | [Deepgram Pricing](https://deepgram.com/pricing) | On Param |
| Rev | [Rev Pricing](https://www.rev.com/pricing) | `api.rev.ai` |
| Speechmatics | [Speechmatics Pricing](https://www.speechmatics.com/pricing) | `eu2.rt.speechmatics.com` |

> ## 👍
>
> Once your credentials are set, you're ready to create your first [Real-Time](https://docs.recall.ai/docs/real-time-transcription) or [Async](https://docs.recall.ai/docs/bot-async-transcription) transcript.

## AWS Transcribe   [Skip link to AWS Transcribe](https://docs.recall.ai/docs/ai-transcription\#aws-transcribe)

### Policies   [Skip link to Policies](https://docs.recall.ai/docs/ai-transcription\#policies)

We typically recommend developers add the default `AmazonTranscribeFullAccess` policy to your AWS IAM User. For a minimal config, ensure that you have the `transcribe:StartStreamTranscription` and `transcribe:StartStreamTranscriptionWebSocket` actions allowed

Below is a minimal policy to have this working

```rdmd-code lang- theme-light
{
    "Version": "2012-10-17",
    "Statement": [\
        {\
            "Sid": "AllowRealtimeStreaming", // Name here is arbitrary\
            "Effect": "Allow",\
            "Action": [\
                "transcribe:StartStreamTranscription",\
                "transcribe:StartStreamTranscriptionWebSocket"\
            ],\
            "Resource": "*"\
        }\
    ]
}

```

Updated 6 days ago

* * *

- [Real-Time Transcription](https://docs.recall.ai/docs/real-time-transcription)
- [Asynchronous Transcription](https://docs.recall.ai/docs/asynchronous-transcription)

Did this page help you?

Yes

No

Ask AI