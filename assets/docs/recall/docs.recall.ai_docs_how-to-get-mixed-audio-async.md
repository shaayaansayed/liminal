---
url: "https://docs.recall.ai/docs/how-to-get-mixed-audio-async"
title: "How to get Mixed Audio MP3 (Async)"
---

This guide is for you if:

- You want to get the meeting recording file as an .mp3

### Platforms Support   [Skip link to Platforms Support](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#platforms-support)

| Platform |  |
| --- | --- |
| Zoom | ✅ |
| Microsoft Teams | ✅ |
| Google Meet | ✅ |
| Webex | ❌ |
| Slack Huddles (Beta) | ❌ |
| Go-To Meeting (Beta) | ❌ |

# Implementation   [Skip link to Implementation](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#implementation)

## Step 1: Create a bot   [Skip link to Step 1: Create a bot](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#step-1-create-a-bot)

To get mixed audio per participant, you must set `recording_config.audio_mixed_raw = {}`. Below is an example of what it would look like in your request

cURLTypeScriptPython

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: YOUR_RECALL_API_KEY' \
     --data '
{
  "meeting_url": "YOUR_MEETING_URL",
  "recording_config": {
    "audio_mixed_mp3": {} # Add this to your request body
  }
}
'

```

```rdmd-code lang-typescript theme-light

const response = await fetch("https://us-east-1.recall.ai/api/v1/bot", {
  method: "POST",
  headers: {
    "accept": "application/json",
    "content-type": "application/json"
    "authorization": "YOUR_RECALL_API_KEY" // Update this
  },
  body: JSON.stringify({
    meeting_url: "YOUR_MEETING_URL", // Update this
    recording_config: {
      audio_mixed_mp3: {} # Add this to your request body
    }
  })
});

if (!response.ok) {
  throw new Error(`Error: ${response.status} ${response.statusText}`);
}

const data = await response.json();

```

```rdmd-code lang-python theme-light

import requests

response = requests.post(
    "https://us-east-1.recall.ai/api/v1/bot",
    json={
      "meeting_url": "YOUR_MEETING_URL", # Update this
      "recording_config": {
		    "audio_mixed_mp3": {} # Add this to your request body
      }
    },
    headers={
      "accept": "application/json",
      "content-type": "application/json",
    	"authorization": "YOUR_RECALL_API_KEY" # Update this
    }
)

if not response.ok:
 	errorMessage = f"Error: {response.status_code} - {response.text}"
  raise requests.RequestException(errorMessage)

result = response.json()

```

## Step 2: Get the recordings for the call   [Skip link to Step 2: Get the recordings for the call](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#step-2-get-the-recordings-for-the-call)

To access these mixed participant audio

First retrieve the existing bot

cURLTypeScriptPython

```rdmd-code lang-curl theme-light

curl --request GET \
     --url https://us-east-1.recall.ai/api/v1/bot/YOUR_RECALL_BOT_ID/ \
     --header 'Authorization: YOUR_RECALL_API_KEY' \
     --header 'accept: application/json'


```

```rdmd-code lang-typescript theme-light

const recall_bot_id = 'YOUR_RECALL_BOT_ID' // Update this
const recall_api_key = 'YOUR_RECALL_API_KEY' // Update this

const get_recall_bot = async (args: { recall_bot_id: string, recall_api_key: string }) => {
    const { recall_bot_id } = args
    const bot_response = await fetch(`https://us-east-1.recall.ai/api/v1/bot/${recall_bot_id}`, {
        method: "GET",
        headers: {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": recall_api_key
        }
    });

    if (!bot_response.ok) {
        throw new Error(`Error: ${bot_response.status} ${bot_response.statusText}`);
    }

    return await bot_response.json();
}

const recall_bot = await get_recall_bot({ recall_bot_id, recall_api_key });

```

```rdmd-code lang-python theme-light

import requests

recall_bot_id = 'YOUR_RECALL_BOT_ID'  # Update this
recall_api_key = 'YOUR_RECALL_API_KEY'  # Update this

def get_recall_bot(args: dict):
    recall_bot_id = args.get("recall_bot_id")
    recall_api_key = args.get("recall_api_key")

    url = f"https://us-east-1.recall.ai/api/v1/bot/{recall_bot_id}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": recall_api_key
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        raise Exception(f"Error: {response.status_code} {response.reason}")

    return response.json()

recall_bot = get_recall_bot({"recall_bot_id": recall_bot_id, "recall_api_key": recall_api_key})

```

The bot will have an array of recordings in the `bot.recording` field as defined in the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) 200 response

Once taken, query the recordings api for the recording id on the bot. This will return a list of medias associated to the recording:

cURLTypeScriptPython

```rdmd-code lang-curl theme-light

curl --request GET \
     --url 'https://us-east-1.recall.ai/api/v1/audio_mixed?recording_id=RECALL_RECORDING_ID' \
     --header 'Authorization: YOUR_RECALL_API_KEY' \
     --header 'accept: application/json'


```

```rdmd-code lang-typescript theme-light

const recall_recording_id = bot.recordings[0].id;

const get_recall_mixed_audio_data = async (args: { recall_recording_id: string, recall_api_key: string }) => {
    const { recall_recording_id, recall_api_key } = args
    const mixed_audio_response = await fetch(
        `https://us-east-1.recall.ai/api/v1/audio_mixed?recording_id=${recall_recording_id}`,
        {
            method: "GET",
            headers: {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": recall_api_key
            }
        }
    );

    if (!mixed_audio_response.ok) {
        throw new Error(`Error: ${mixed_audio_response.status} ${mixed_audio_response.statusText}`);
    }

    return await mixed_audio_response.json()
}

const mixed_audio_data = await get_recall_mixed_audio_data({
  recall_recording_id: recall_bot.recordings[0].id,
  recall_api_key
})

```

```rdmd-code lang-python theme-light

recall_recording_id = recall_bot["recordings"][0]["id"]

def get_recall_mixed_audio_data(args: dict):
    recall_recording_id = args.get("recall_recording_id")
    recall_api_key = args.get("recall_api_key")

    url = f"https://us-east-1.recall.ai/api/v1/audio_mixed?recording_id={recall_recording_id}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": recall_api_key
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        raise Exception(f"Error: {response.status_code} {response.reason}")

    return response.json()

mixed_audio_data = get_recall_mixed_audio_data({
    "recall_recording_id": recall_recording_id,
    "recall_api_key": recall_api_key
})

```

The `mixed_audio_response` schema is defined in the [List Audio Mixed](https://docs.recall.ai/reference/audio_mixed_list) 200 response

## Step 3: Accessing mp3   [Skip link to Step 3: Accessing mp3](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#step-3-accessing-mp3)

Now that you have the recordings list, you can get the download URL and query the data:

TypeScriptPython

```rdmd-code lang-typescript theme-light

const get_recall_mixed_audio_parts = async (args: { mixed_audio_data: any }) => {
    const { mixed_audio_data } = args;
    const audios = mixed_audio_data.results;

    for (const audio of audios) {
        const download_url = audio.data.download_url
        console.log(download_url)
    }

    return audios
}

const mixed_audio_parts = await get_recall_mixed_audio_parts({ mixed_audio_data })

```

```rdmd-code lang-python theme-light

import asyncio
from typing import Any, Dict, List

async def get_recall_mixed_audio_parts(mixed_audio_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract each audio part’s download URL from Recall’s mixed-audio payload."""
    audios = mixed_audio_data["results"]

    for audio in audios:
        download_url = audio["data"]["download_url"]
        print(download_url)

    return audios

```

The `mixed_audio_parts` will be the media binary

### Downloading media binary   [Skip link to Downloading media binary](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#downloading-media-binary)

You can also download the audio media binary like so:

## Full Script   [Skip link to Full Script](https://docs.recall.ai/docs/how-to-get-mixed-audio-async\#full-script)

TypeScript

```rdmd-code lang-typescript theme-light

import fs from 'fs';
import { env } from '../env';

const recall_api_key = ''
const recall_bot_id = ''

interface MixedAudioResponse {
    next: null;
    previous: null;
    results: Array<{
        id: string;
        recording: {
            id: string;
            metadata: Record<string, any>;
        };
        created_at: string;
        status: {
            code: 'done';
            sub_code: null;
            updated_at: string;
        };
        metadata: Record<string, any>;
        data: {
            download_url: string;
        };
        format: string;
    }>;
}

export const start = async () => {
    const recall_bot = await get_recall_bot({ recall_bot_id, recall_api_key });
    const mixed_audio_data = await get_recall_mixed_audio_data({ recall_recording_id: recall_bot.recordings[0].id, recall_api_key })
    const mixed_audio_parts = await get_recall_mixed_audio_parts({ mixed_audio_data })
    console.log(JSON.stringify(mixed_audio_parts, null, 2))
};

const get_recall_bot = async (args: { recall_bot_id: string, recall_api_key: string }) => {
    const { recall_bot_id } = args
    const bot_response = await fetch(`https://us-east-1.recall.ai/api/v1/bot/${recall_bot_id}`, {
        method: "GET",
        headers: {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": recall_api_key
        }
    });

    if (!bot_response.ok) {
        throw new Error(`Error: ${bot_response.status} ${bot_response.statusText}`);
    }

    return await bot_response.json();
}

const get_recall_mixed_audio_data = async (args: { recall_recording_id: string, recall_api_key: string }) => {
    const { recall_recording_id, recall_api_key } = args
    const mixed_audio_response = await fetch(
        `https://us-east-1.recall.ai/api/v1/audio_mixed?recording_id=${recall_recording_id}`,
        {
            method: "GET",
            headers: {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": recall_api_key
            }
        }
    );

    if (!mixed_audio_response.ok) {
        throw new Error(`Error: ${mixed_audio_response.status} ${mixed_audio_response.statusText}`);
    }

    return await mixed_audio_response.json()
}

const get_recall_mixed_audio_parts = async (args: { mixed_audio_data: any }) => {
    const { mixed_audio_data } = args;
    const audios = mixed_audio_data.results;

    for (const audio of audios) {
        const download_url = audio.data.download_url
        const file_path = `./mixed_audio.mp3`
        download_and_process_file({ download_url, file_path })
    }

    return audios
}

async function download_and_process_file(args: { download_url: string, file_path: string }) {
    try {
        const { download_url, file_path } = args;
        const response = await fetch(download_url);

        if (!response.ok) {
            throw new Error(`Failed to download file: ${response.status} ${response.statusText}`);
        }

        const fileStream = fs.createWriteStream(file_path);

        // For binary data, we need to use response.arrayBuffer() and write the buffer
        const buffer = await response.arrayBuffer();
        const uint8Array = new Uint8Array(buffer);
        fileStream.write(uint8Array);
        fileStream.end();

        return new Promise((resolve, reject) => {
            fileStream.on('finish', () => {
                console.log(`File saved to ${file_path}`);
                resolve(file_path);
            });

            fileStream.on('error', (error) => {
                console.error(`Error saving file: ${error}`);
                reject(error);
            });
        });
    } catch (error) {
        console.error(`Error downloading the file: ${error}`);
        throw error;
    }
}

start();

```

Updated 10 days ago

* * *

Did this page help you?

Yes

No

Ask AI