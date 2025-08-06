---
url: "https://docs.recall.ai/reference/bot_start_recording_create"
title: "Start Recording"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  Important: Recording Settings Override Bot Defaults
>
> When you invoke this endpoint, any options you include in the POST request will directly determine the recording's settings. If you omit a parameter, the endpoint applies its own default value— **not** the one from your bot’s configuration.
>
> Tip: To ensure that your manual recordings match your bot's settings, explicitly specify all desired recording options in your request.

For more information on bot recording behavior using this endpoint, see [Recording Control](https://docs.recall.ai/docs/recording-control#start--stop-recording)

id

uuid

required

A UUID string identifying this bot.

transcript

object \| null

Specify this to capture transcript of the meeting as part of the recording. **[Read more in this guide](https://docs.recall.ai/docs/bot-real-time-transcription)**

Default: `null`

transcript object \| null

realtime\_endpoints

array

Defaults to

Add endpoints here to receive data (e.g transcript, participant events) from the recording in realtime during the meeting.

Default: `[]`

realtime\_endpoints
ADD

retention

Specify the retention policy for the recording. **[Read more in this guide](https://docs.recall.ai/docs/storage-and-playback)**

timed

forever

video\_mixed\_layout

string

Defaults to speaker\_view

- `speaker_view` \- speaker\_view
- `gallery_view` \- gallery\_view
- `gallery_view_v2` \- gallery\_view\_v2
- `audio_only` \- audio\_only

speaker\_viewgallery\_viewgallery\_view\_v2audio\_only

video\_mixed\_mp4

object \| null

Capture mixed video of the meeting as part of the recording. **This is enabled by default**.

Default: `{}`

video\_mixed\_mp4 object \| null

participant\_events

object \| null

Capture participant events as part of the recording. **This is enabled by default**.

Default: `{}`

participant\_events object \| null

meeting\_metadata

object \| null

Capture meeting metadata as part of the recording. **This is enabled by default**.

Default: `{}`

meeting\_metadata object \| null

video\_mixed\_participant\_video\_when\_screenshare

string

Defaults to overlap

- `hide` \- hide
- `beside` \- beside
- `overlap` \- overlap

hidebesideoverlap

start\_recording\_on

string

Defaults to participant\_join

- `call_join` \- call\_join
- `participant_join` \- participant\_join
- `participant_speak` \- participant\_speak

call\_joinparticipant\_joinparticipant\_speak

include\_bot\_in\_recording

object

include\_bot\_in\_recording object

metadata

object

metadata object

audio\_mixed\_raw

object \| null

Specify this to capture mixed audio in raw format of the meeting.

Default: `null`

audio\_mixed\_raw object \| null

audio\_mixed\_mp3

object \| null

Specify this to capture mixed audio in the mp3 format of the meeting

Default: `null`

audio\_mixed\_mp3 object \| null

video\_separate\_mp4

object \| null

Specify this to capture separate video in mp4 format for each participant in the meeting. Only supported with video\_mixed\_layout='gallery\_view\_v2'. **[Read more in this guide](https://docs.recall.ai/docs/separate-video-streams)**

Default: `null`

video\_separate\_mp4 object \| null

audio\_separate\_raw

object \| null

Specify this to capture separate audio in raw format for each participant in the meeting( **limited support**). **[Read more in this guide](https://docs.recall.ai/docs/separate-audio-streams)**

Default: `null`

audio\_separate\_raw object \| null

video\_mixed\_flv

object \| null

Specify this to capture mixed video in flv format(\*\*required for rtmp streaming).

Default: `null`

video\_mixed\_flv object \| null

video\_separate\_png

object \| null

Specify this to capture separate video in png format for each participant in the meeting. Only supported with video\_mixed\_layout='gallery\_view\_v2'. **[Read more in this guide](https://docs.recall.ai/docs/separate-video-streams)**

Default: `null`

video\_separate\_png object \| null

# `` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/bot/{id}/start\_recording/

```

xxxxxxxxxx

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/bot/id/start_recording/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 3 months ago

* * *

Did this page help you?

Yes

No