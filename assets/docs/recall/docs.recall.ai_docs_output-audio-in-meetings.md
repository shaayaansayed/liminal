---
url: "https://docs.recall.ai/docs/output-audio-in-meetings"
title: "Output Audio"
---

There are two primary methods of outputting audio from bots:

- **Automatic audio output**
- **Calling the [Output Audio](https://docs.recall.ai/reference/bot_output_audio_create) endpoint**

Streaming audio into a call is can now be done with [Output Media](https://docs.recall.ai/docs/stream-media)

## Platform Support   [Skip link to Platform Support](https://docs.recall.ai/docs/output-audio-in-meetings\#platform-support)

| Platform | Available |
| --- | --- |
| \*Zoom | ✅ |
| Google Meet | ✅ |
| Microsoft Teams | ✅ |
| Cisco Webex | ✅ |
| Slack Huddles | ❌ |

_\*Zoom Native not yet supported._

## Audio Format   [Skip link to Audio Format](https://docs.recall.ai/docs/output-audio-in-meetings\#audio-format)

Audio should be provided as an mp3 encoded as a base 64 string.

MP3 files can easily be converted to a b64 string using CLI tools such as [ffmpeg](https://ffmpeg.org/) or an online tool such as [b64Guru](https://base64.guru/converter/encode/audio/mp3).

# Outputting Audio   [Skip link to Outputting Audio](https://docs.recall.ai/docs/output-audio-in-meetings\#outputting-audio)

* * *

## Using `automatic_audio_output`   [Skip link to Using ](https://docs.recall.ai/docs/output-audio-in-meetings\#using-automatic_audio_output)

[Create Bot](https://docs.recall.ai/reference/bot_create) accepts an `automatic_audio_output` configuration for automatically outputting audio when the bot starts recording, with the option to repeat the audio when participants join.

`data` allows you to specify the mp3 the bot should play.

- `kind` \- The type of data encoded in the b64 string (Currently only `mp3` is supported)
- `b64_data` \- Data encoded in Base64 format, using the standard alphabet (as specified [here](https://datatracker.ietf.org/doc/html/rfc4648#section-4))

`replay_on_participant_join` can be optionally used to repeat the audio whenever someone joins.

- `debounce_mode`: Debounce mode ("trailing" or "leading")

  - `leading`: The debounce timer will start counting down when the first participant joins.
  - `trailing`: The debounce timer will start counting down when the last participant joins.
- `debounce_interval`: The amount of time to wait for additional participants to join before replaying the audio.
- `disable_after`: The number of seconds after which the audio will no longer replay when new participants join. This parameter is useful to prevent the bot from interrupting a meeting, if a late participant joins.

**`automatic_audio_output` example**

JSON

```rdmd-code lang-json theme-light

// POST https://us-east-1.recall.ai/api/v1/bot/
{
  "automatic_audio_output": {
    "in_call_recording": {
      "data": {
        "kind": "mp3",
        "b64_data": "..."
      },
      "replay_on_participant_join": {
        "debounce_mode": "trailing",
        "debounce_interval": 10,
        "disable_after": 60
      }
    }
  },
  ...
}

```

Using the above configuration as an example, let's say we have the following scenario:

- Participant 1 is there a bit early and joins right before the bot starts recording.
- 5 seconds after recording starts, Participant 2 joins.
- 5 seconds later, Participant 3 joins.
- Participant 4 is running late, and joins the call three minutes after recording starts.

In this scenario, Participants 1 and 4's experiences are fairly straightforward.

- Participant 1 hears the audio played when the bot starts recording.
- Participant 4 never hears the audio played since they joined 180 seconds after the bot started recording, which is greater than the `disabled_after` value of 60.

Participants 2 and 3 will experience something slightly different based on the `debounce_mode`:

- In `trailing` mode, the audio would play 10 seconds after Participant 3 joins (15 seconds after Participant 2 joins).
- If we set the `debounce_mode` to `leading`, however, the audio will play 10 seconds after Participant 2 joins (5 seconds after Participant 3 joins).

## Using the Output Audio endpoint   [Skip link to Using the Output Audio endpoint](https://docs.recall.ai/docs/output-audio-in-meetings\#using-the-output-audio-endpoint)

If your use case requires more manual control over outputting bot audio, you can use the [Output Audio](https://docs.recall.ai/reference/bot_output_audio_create) endpoint.

This endpoint takes the same parameters as the bot configuration objects above:

```rdmd-code lang- theme-light
// POST https://us-east-1.recall.ai/api/v1/bot/{id}/output_audio/
{
  "kind": "mp3",
  "b64_data": "..." // b64 encoded string
}

```

> ## 📘
>
> To use the [Output Audio](https://docs.recall.ai/reference/bot_output_audio_create) endpoint, currently bots must be configured with an `automatic_audio_output` in the [Create Bot](https://docs.recall.ai/reference/bot_create) request.
>
> If you do not wish to leverage any automatic audio output, and just want to use the endpoint, we recommend adding a short silent mp3 file as the `b64_data` in this configuration.

Updated 3 months ago

* * *

Did this page help you?

Yes

No

Ask AI