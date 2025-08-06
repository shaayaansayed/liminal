---
url: "https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async"
title: "How to get Separate Videos per Participant (Async)"
---

> ## 📘  Separate videos per participant does not include audio

This guide is for you if:

- You want to get separate recording files for each participant
- You want to analyze each participant in the call individually

### Platforms Support   [Skip link to Platforms Support](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#platforms-support)

| Platform |  |
| --- | --- |
| Zoom | ✅ |
| Microsoft Teams | ✅ |
| Google Meet | ✅ |
| Webex | ❌ |
| Slack Huddles (Beta) | ✅ |
| Go-To Meeting (Beta) | ✅ |

### Recording Specifications   [Skip link to Recording Specifications](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#recording-specifications)

|  | Resolution | Frame Rate |
| --- | --- | --- |
| Screen Share Video | 360p | From meeting provider, can vary |
| Participant Video | 360p | From meeting provider, can vary |

# Implementation   [Skip link to Implementation](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#implementation)

## Step 1: Create a bot   [Skip link to Step 1: Create a bot](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#step-1-create-a-bot)

To get separate video per participant, you must set `recording_config.video_mixed_layout = "gallery_view_v2"` and `recording_config.video_separate_mp4 = {}`. Below is an example of what it would look like in your request

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
    "video_mixed_layout": "gallery_view_v2", # Add this to your request body
    "video_separate_mp4": {} # Add this to your request body
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
      video_mixed_layout: "gallery_view_v2", // Add this to your request body
      video_separate_mp4: {} # Add this to your request body
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
	      "video_mixed_layout": "gallery_view_v2" # Add this to your request body
		    "video_separate_mp4": {} # Add this to your request body
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

## Step 2: Get the recordings for the call   [Skip link to Step 2: Get the recordings for the call](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#step-2-get-the-recordings-for-the-call)

To access these separate participant video

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
     --url 'https://us-east-1.recall.ai/api/v1/video_separate?recording_id=RECALL_RECORDING_ID' \
     --header 'Authorization: YOUR_RECALL_API_KEY' \
     --header 'accept: application/json'


```

```rdmd-code lang-typescript theme-light

const recall_recording_id = bot.recordings[0].id;

const get_recall_separate_video_data = async (args: { recall_recording_id: string, recall_api_key: string }) => {
    const { recall_recording_id, recall_api_key } = args
    const separate_video_response = await fetch(
        `https://us-east-1.recall.ai/api/v1/video_separate?recording_id=${recall_recording_id}`,
        {
            method: "GET",
            headers: {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": recall_api_key
            }
        }
    );

    if (!separate_video_response.ok) {
        throw new Error(`Error: ${separate_video_response.status} ${separate_video_response.statusText}`);
    }

    return await separate_video_response.json()
}

const separate_video_data = await get_recall_separate_video_data({
  recall_recording_id: recall_bot.recordings[0].id,
  recall_api_key
})

```

```rdmd-code lang-python theme-light

recall_recording_id = recall_bot["recordings"][0]["id"]

def get_recall_separate_video_data(args: dict):
    recall_recording_id = args.get("recall_recording_id")
    recall_api_key = args.get("recall_api_key")

    url = f"https://us-east-1.recall.ai/api/v1/video_separate?recording_id={recall_recording_id}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": recall_api_key
    }

    response = requests.get(url, headers=headers)

    if not response.ok:
        raise Exception(f"Error: {response.status_code} {response.reason}")

    return response.json()

separate_video_data = get_recall_separate_video_data({
    "recall_recording_id": recall_recording_id,
    "recall_api_key": recall_api_key
})

```

The `separate_video_response` schema is defined in the [List Video Separate](https://docs.recall.ai/reference/video_separate_list) 200 response. Only participants who turned their video on during the call will have data populated in the response from this endpoint.

## Step 3: Accessing separate participant video   [Skip link to Step 3: Accessing separate participant video](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#step-3-accessing-separate-participant-video)

Now that you have the recordings list, you can filter for the separate participant videos and query the data:

TypeScriptPython

```rdmd-code lang-typescript theme-light

const get_recall_separate_video_parts = async (args: { separate_video_data: SeparateVideoResponse }) => {
    const { separate_video_data } = args;
    const videos = separate_video_data.results;

    const video_parts = Promise.all(
        videos.map(async (video) => {
            const response = await fetch(video.data.download_url);

            if (!response.ok) {
                throw new Error(`Error: ${response.status} ${response.statusText}`);
            }

            return await response.json();
        })
    );
    return video_parts;
}

const separate_video_parts = await get_recall_separate_video_parts({ separate_video_data })

```

```rdmd-code lang-python theme-light

unmixed_videos = [media for media in separate_video_response.results if media["type"] == "mp4_video_mixed"]

import requests

def get_recall_separate_video_parts(args: dict):
    separate_video_data = args.get("separate_video_data")
    videos = separate_video_data["results"]

    video_parts = []
    for video in videos:
        download_url = video["data"]["download_url"]
        response = requests.get(download_url)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} {response.reason}")

        video_parts.append(response.json())

    return video_parts

separate_video_parts = get_recall_separate_video_parts({"separate_video_data": separate_video_data})

```

The `separate_video_parts` will look like the schema defined in [Participant Separate Video Parts JSON](https://beta-docs.recall.ai/docs/download-urls#json-participant-separate-video-parts)

### Downloading media binary   [Skip link to Downloading media binary](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#downloading-media-binary)

You can also download the video media binary like so:

TypeScriptPython

```rdmd-code lang-typescript theme-light

import fs from 'fs';

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

const unmixed_video_part = separate_video_parts[0]
	?.find((video_part: any) => video_part.participant.is_host = true);
const unmixed_video_part_download_url = unmixed_video_part.download_url
download_and_process_file({
  download_url: unmixed_video_part_download_url,
  file_path: './unmixed_video.mp4'
});

```

```rdmd-code lang-python theme-light

import requests

def download_and_process_file(args: dict):
    try:
        download_url = args.get("download_url")
        file_path = args.get("file_path")

        # Send the request to download the file
        response = requests.get(download_url, stream=True)
        if response.status_code != 200:
            raise Exception(f"Failed to download file: {response.status_code} {response.reason}")

        # Save the file
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    file.write(chunk)

        print(f"File saved to {file_path}")
        return file_path
    except Exception as error:
        print(f"Error downloading the file: {error}")
        raise

# Example usage
unmixed_video_part = next(
    (video_part for video_part in separate_video_parts[0] if video_part["participant"]["is_host"] == True),
    None
)

if unmixed_video_part:
    unmixed_video_part_download_url = unmixed_video_part["download_url"]
    file_path = "./unmixed_video.mp4"
    download_and_process_file({"download_url": unmixed_video_part_download_url, "file_path": file_path})

```

## Full Script   [Skip link to Full Script](https://docs.recall.ai/docs/how-to-get-separate-videos-per-participant-async\#full-script)

TypeScript

```rdmd-code lang-typescript theme-light

import fs from 'fs';

const recall_api_key = 'YOUR_RECALL_API_KEY'
const recall_bot_id = 'YOUR_RECALL_BOT_ID'

interface SeparateVideoResponse {
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

const start = async () => {
    const recall_bot = await get_recall_bot({ recall_bot_id, recall_api_key });
    const separate_video_data = await get_recall_separate_video_data({ recall_recording_id: recall_bot.recordings[0].id, recall_api_key })
    const separate_video_parts = await get_recall_separate_video_parts({ separate_video_data })

    // Download the unmixed video
    const is_host = false;
    const unmixed_video_part = separate_video_parts[0]
        ?.find((video_part: any) => video_part.participant.is_host === is_host);
    const unmixed_video_part_download_url = unmixed_video_part.download_url
    download_and_process_file({ download_url: unmixed_video_part_download_url, file_path: `./unmixed_video-${unmixed_video_part.participant.is_host ? 'host' : 'guest'}.mp4` });

    console.log(JSON.stringify(separate_video_parts, null, 2))
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

const get_recall_separate_video_data = async (args: { recall_recording_id: string, recall_api_key: string }) => {
    const { recall_recording_id, recall_api_key } = args
    const separate_video_response = await fetch(
        `https://us-east-1.recall.ai/api/v1/video_separate?recording_id=${recall_recording_id}`,
        {
            method: "GET",
            headers: {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": recall_api_key
            }
        }
    );

    if (!separate_video_response.ok) {
        throw new Error(`Error: ${separate_video_response.status} ${separate_video_response.statusText}`);
    }

    return await separate_video_response.json()
}

const get_recall_separate_video_parts = async (args: { separate_video_data: SeparateVideoResponse }) => {
    const { separate_video_data } = args;
    const videos = separate_video_data.results;

    const video_parts = Promise.all(
        videos.map(async (video) => {
            const response = await fetch(video.data.download_url);

            if (!response.ok) {
                throw new Error(`Error: ${response.status} ${response.statusText}`);
            }

            return await response.json();
        })
    );
    return video_parts;
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

start()

```

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Ask AI