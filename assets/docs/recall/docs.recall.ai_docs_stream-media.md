---
url: "https://docs.recall.ai/docs/stream-media"
title: "Stream Audio/Video from Webpage to a Meeting"
---

Recall supports streaming a webpage's audio and video to meetings via the bot's camera and microphone. This set of APIs is the perfect combination to build interactive AI agents that listen to the meeting and react in realtime. Some of our customers use this functionality to build AI-powered sales agents, coaches, recruiters, meeting planners and more.

For example implementations/use cases, see our demo repos:

- [AI Voice Agent Demo](https://github.com/recallai/voice-agent-demo)
- [Real-time Translator Demo](https://github.com/recallai/real-time-translator-demo)

## A specific example   [Skip link to A specific example](https://docs.recall.ai/docs/stream-media\#a-specific-example)

The following video demonstration shows an example of a bot reacting in real time to the conversation in the meeting.

cerebras demo

![](https://cdn.loom.com/avatars/29919248_04449db3c0b54fa3aed2eb2cc18e704c_192.jpg)

[cerebras demo](https://www.loom.com/share/bafb9727c2e049b2b55e07be0ff7bd80?source=embed_watch_on_loom_cta "cerebras demo")

2 min

1.52K views

2

[Open video in Loom](https://www.loom.com/share/bafb9727c2e049b2b55e07be0ff7bd80?source=embed_watch_on_loom_cta "Open video in Loom")

1.2×

1 min 39 sec⚡️2 min 4 sec1 min 39 sec1 min 23 sec1 min 6 sec58 sec49 sec39 sec

👎

Anonymous

😍

Elliot Levin

😮

Anonymous

😂

Sumi Uzir

👍

Pranav

😮

Pranav

🙌

Pranav

😍

Pranav

2

![](https://cdn.loom.com/avatars/6572566_c686a3f9ce1150bb1c2b05e162e7b75b_192.jpg)

Thank you, Antonio! 🙏
+1 other comment

Your user agent does not support the HTML5 Video element.

![](https://cdn.loom.com/avatars/29919248_04449db3c0b54fa3aed2eb2cc18e704c_192.jpg)

[cerebras demo](https://www.loom.com/share/bafb9727c2e049b2b55e07be0ff7bd80?source=embed_watch_on_loom_cta "cerebras demo")

2 min

1.52K views

2

[Open video in Loom](https://www.loom.com/share/bafb9727c2e049b2b55e07be0ff7bd80?source=embed_watch_on_loom_cta "Open video in Loom")

1.2×

1 min 39 sec⚡️2 min 4 sec1 min 39 sec1 min 23 sec1 min 6 sec58 sec49 sec39 sec

👎

Anonymous

😍

Elliot Levin

😮

Anonymous

😂

Sumi Uzir

👍

Pranav

😮

Pranav

🙌

Pranav

😍

Pranav

2

![](https://cdn.loom.com/avatars/6572566_c686a3f9ce1150bb1c2b05e162e7b75b_192.jpg)

Thank you, Antonio! 🙏
+1 other comment

# Platform Support   [Skip link to Platform Support](https://docs.recall.ai/docs/stream-media\#platform-support)

| Platform | Bot Configuration ( `output_media`) |
| --- | --- |
| Zoom\* | ✅ |
| Google Meet | ✅ |
| Microsoft Teams | ✅ |
| Cisco Webex | ✅ |
| Slack Huddles | ❌ |

_\*Zoom native bot not supported_

> ## 🚧  Streaming Media incompatible with [`automatic_video_output`](https://docs.recall.ai/docs/output-video-in-meetings) and [`automatic_audio_output`](https://docs.recall.ai/docs/output-audio-in-meetings)
>
> Bot Media Output cannot currently be used with [`automatic_video_output`](https://docs.recall.ai/docs/output-video-in-meetings) or [`automatic_audio_output`](https://docs.recall.ai/docs/output-audio-in-meetings).
>
> The [Output Video](https://docs.recall.ai/reference/bot_output_video_create) and [Output Audio](https://docs.recall.ai/reference/bot_output_audio_create) endpoints must also **not** be used if your bot is streaming a webpage's contents to the meeting.

# Quickstart   [Skip link to Quickstart](https://docs.recall.ai/docs/stream-media\#quickstart)

* * *

## Streaming a webpage's audio/video to a meeting   [Skip link to Streaming a webpage's audio/video to a meeting](https://docs.recall.ai/docs/stream-media\#streaming-a-webpages-audiovideo-to-a-meeting)

### Method 1: Using `output_media` in [Create Bot](https://docs.recall.ai/reference/bot_create)   [Skip link to Method 1: Using ](https://docs.recall.ai/docs/stream-media\#method-1-using-output_media-in--create-bot)

You can use the `output_media` configuration in the [Create Bot](https://docs.recall.ai/reference/bot_create) endpoint to stream the audio and video contents of a webpage to your meeting.

`output_media` takes the following parameters:

- `kind`: The type of media to stream (currently only `webpage` is supported)
- `config`: The webpage configuration (currently only supports `url`)

Let's look at an example call to [Create Bot](https://docs.recall.ai/reference/bot_create):

JSON

```rdmd-code lang-json theme-light

// POST /api/v1/bot/
{
  "meeting_url": "https://us02web.zoom.us/j/1234567890",
  "bot_name": "Recall.ai Notetaker",
  "output_media": {
    "camera": {
      "kind": "webpage",
      "config": {
        "url": "https://www.recall.ai"
      }
    }
  }
}

```

The example above tells Recall to create a bot that will continuously stream the contents of [recall.ai](https://www..recall.ai/) to the provided meeting URL.

### Method 2: Using the [Output Media](https://docs.recall.ai/reference/bot_output_media_create) endpoint   [Skip link to Method 2: Using the ](https://docs.recall.ai/docs/stream-media\#method-2-using-the-output-media-endpoint)

You can choose to start outputting media by calling the [Output Media](https://docs.recall.ai/reference/bot_output_media_create) endpoint at any point when the bot is in a call.

The parameters for the request are the same as the `output_media` configuration.

**Example cURL:**

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://api.recall.ai/api/v1/bot/{bot_id}/output_media/ \
     --header 'Authorization: ${RECALL_API_KEY}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data-raw '
{
	"camera": {
    "kind": "webpage",
    "config": {
      "url": "https://recall.ai"
    }
  }
}
'

```

#### Stopping media output   [Skip link to Stopping media output](https://docs.recall.ai/docs/stream-media\#stopping-media-output)

You can stop the bot media output at any point while the bot is streaming media to a call by calling the [Stop Output Media](https://docs.recall.ai/reference/bot_output_video_destroy) endpoint.

**Example cURL:**

cURL

```rdmd-code lang-curl theme-light

curl --request DELETE \
     --url https://api.recall.ai/api/v1/bot/{bot_id}/output_media/ \
     --header 'Authorization: ${RECALL_API_KEY}' \
     --header 'accept: application/json' \
     --header 'content-type: application/json'
     --data-raw '{ "camera": true }'

```

## Accessing realtime meeting data   [Skip link to Accessing realtime meeting data](https://docs.recall.ai/docs/stream-media\#accessing-realtime-meeting-data)

The bot exposes a Websocket endpoint to retrieve realtime meeting data while the webpage is streaming audio and video to the call. Right now, only realtime transcripts are supported. You can connect to the realtime API from your webpage with the following example:

JavaScript

```rdmd-code lang-javascript theme-light

const ws = new WebSocket('wss://meeting-data.bot.recall.ai/api/v1/transcript');

ws.onmessage = (event) => {
  const message = JSON.parse(event.data).transcript?.words?.map(l => l.text)?.join(' ');

  // .. your logic to handle realtime transcripts
};

ws.onopen = () => {
  console.log('Connected to WebSocket server');
};

ws.onclose = () => {
  console.log('Disconnected from WebSocket server');
};

```

The websocket messages coming from the `/api/v1/transcript` endpoint have the same shape as the `data` object in [Real-time transcription](https://docs.recall.ai/docs/real-time-transcription#events) .

## Piping the meeting audio to the webpage   [Skip link to Piping the meeting audio to the webpage](https://docs.recall.ai/docs/stream-media\#piping-the-meeting-audio-to-the-webpage)

Output media bots configure an input device inside the running webpage that receives the mixed meeting audio of all participants.

You can access a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream) object and its audio track from the webpage running inside the bot. The following example shows how to get samples of the meeting audio in [`AudioData`](https://developer.mozilla.org/en-US/docs/Web/API/AudioData) objects:

javascript

```rdmd-code lang-javascript theme-light

const mediaStream =   await navigator.mediaDevices.getUserMedia({ audio: true });
const meetingAudioTrack = mediaStream.getAudioTracks()[0];

const trackProcessor = new MediaStreamTrackProcessor({ track: meetingAudioTrack });
const trackReader = trackProcessor.readable.getReader();

while (true) {
  const { value, done } = await trackReader.read();
  const audioData = value;
  ... // Do something with the audio data
}

```

# Debugging   [Skip link to Debugging](https://docs.recall.ai/docs/stream-media\#debugging)

* * *

## Debugging your webpage with remote Devtools   [Skip link to Debugging your webpage with remote Devtools](https://docs.recall.ai/docs/stream-media\#debugging-your-webpage-with-remote-devtools)

During the development process, you may need to debug your output media bot's webpage. Recall provides an easy way to connect to the webpage's [Chrome Devtools](https://developer.chrome.com/docs/devtools) while the bot is running. Check the video demo below and read the following instructions to learn how to access your bot's Devtools.

Debugging Live Output Media Bots with Recall.ai 🤖

![](https://cdn.loom.com/avatars/29919248_04449db3c0b54fa3aed2eb2cc18e704c_192.jpg)

[Debugging Live Output Media Bots with Recall.ai 🤖](https://www.loom.com/share/88268f164d164e809faba0befcb3b5c4?source=embed_watch_on_loom_cta "Debugging Live Output Media Bots with Recall.ai 🤖")

2 min

337 views

1

[Open video in Loom](https://www.loom.com/share/88268f164d164e809faba0befcb3b5c4?source=embed_watch_on_loom_cta "Open video in Loom")

1.2×

1 min 35 sec⚡️1 min 59 sec1 min 35 sec1 min 19 sec1 min 3 sec56 sec47 sec38 sec

😍

Elliot Levin

😍

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

🙌

Elliot Levin

🙌

Elliot Levin

🙌

Elliot Levin

😍

David Gu

😍

David Gu

🙌

David Gu

🙌

David Gu

🔥

Jake Miyazaki

😱

Vishal Pugazhendhi

![](https://cdn.loom.com/avatars/22254965_fd7999d686f346c4b1dcfb8eec1d6e2c_192.jpg)

This is so cool! Amazing work!

Your user agent does not support the HTML5 Video element.

![](https://cdn.loom.com/avatars/29919248_04449db3c0b54fa3aed2eb2cc18e704c_192.jpg)

[Debugging Live Output Media Bots with Recall.ai 🤖](https://www.loom.com/share/88268f164d164e809faba0befcb3b5c4?source=embed_watch_on_loom_cta "Debugging Live Output Media Bots with Recall.ai 🤖")

2 min

337 views

1

[Open video in Loom](https://www.loom.com/share/88268f164d164e809faba0befcb3b5c4?source=embed_watch_on_loom_cta "Open video in Loom")

1.2×

1 min 35 sec⚡️1 min 59 sec1 min 35 sec1 min 19 sec1 min 3 sec56 sec47 sec38 sec

😍

Elliot Levin

😍

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

😮

Elliot Levin

🙌

Elliot Levin

🙌

Elliot Levin

🙌

Elliot Levin

😍

David Gu

😍

David Gu

🙌

David Gu

🙌

David Gu

🔥

Jake Miyazaki

😱

Vishal Pugazhendhi

![](https://cdn.loom.com/avatars/22254965_fd7999d686f346c4b1dcfb8eec1d6e2c_192.jpg)

This is so cool! Amazing work!

1. Send an output media bot to your meeting, and wait for its output media stream
2. [Log in](https://www.recall.ai/login) to your Recall.ai dashboard
3. Select Bot Explorer in the sidebar
4. In the Bot Explorer app, search for your bot by ID

![](https://files.readme.io/45ba45d4f1d96e38c59e91b37ae4325c5066d21f8193a8a9ec98888ffa6dced7-image.png)

5. Open the "Debug Data" tab for your bot then under CPU Metrics, click the "Open Remote Devtools" button. A devtools inspector connected to your live bot will open in a new tab
![](https://files.readme.io/12013f339d96e728aa6177faed2ab9d9d789f2012cdf43ee384d9904ccd562e3-CleanShot_2025-04-11_at_13.23.082x.png)

> ## 📘  Bot must be alive
>
> Since Output Media Devtools are exposed by the bot itself and CPU metrics are in real-time, they are only available when the bot is actively in a call.

You can also view the CPU usage for an individual bot in the "Bot Details" section. You can use this graph to uncover any performance bottlenecks with your webpage which might be causing the webpage to lag or perform poorly.

![](https://files.readme.io/2003b2475688e3109aeb12172426f2a153f5d276931e3bd0528209714f796c6a-CleanShot_2024-12-09_at_11.36.22.png)

## Addressing audio and video issues: bot variants   [Skip link to Addressing audio and video issues: bot variants](https://docs.recall.ai/docs/stream-media\#addressing-audio-and-video-issues-bot-variants)

While we expose CPU metrics to help you identify and address any performance issues on your end, sometimes this is out of your control and you just need more CPU power or hardware acceleration.

The streaming media functionality runs in isolation from the bot producing the final meeting recording. Below is a breakdown of the compute resources available to the instance running your webpage:

| Variant | CPU | Memory | WebGL |
| --- | --- | --- | --- |
| `web` (default) | 250 millicores | 750MB | ❌ Unsupported |
| `web_4_core` | 2250 millicores | 5250MB | ❌ Unsupported |
| `web_gpu` | 6000 millicores | 13250MB | ✅ Supported |
| `native` | ❌ Unsupported | ❌ Unsupported | ❌ Unsupported |

To use these configurations, you can specify the `variant` in your [Create Bot](https://docs.recall.ai/reference/bot_create) request:

JSON

```rdmd-code lang-json theme-light

{
  ...
  "variant": {
    "zoom": "web_4_core",
    "google_meet": "web_4_core",
    "microsoft_teams": "web_4_core"
  }
}

```

These bots run on larger machines, which can help address any CPU bottlenecks hindering the audio & video quality of your Output Media feature.

> ## ❗️  Important
>
> Due to the inherent cost of running larger machines, the prices for some variants are higher:
>
> | Variant | Pay-as-you-go plan | Monthly plans |
> | --- | --- | --- |
> | `web_4_core` | $1.10/hour | standard bot usage rate + $0.10/hour |
> | `web_gpu` | $2.00/hour | standard bot usage rate + $1.00/hour |

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/stream-media\#faq)

* * *

## What are the browser dimensions of the webpage?   [Skip link to What are the browser dimensions of the webpage?](https://docs.recall.ai/docs/stream-media\#what-are-the-browser-dimensions-of-the-webpage)

1280x720px

## How can I test my bot?   [Skip link to How can I test my bot?](https://docs.recall.ai/docs/stream-media\#how-can-i-test-my-bot)

You can use `ngrok` to test your bot. We will add the `ngrok-skip-browser-warning: true` to bypass the ngrok warning.

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI