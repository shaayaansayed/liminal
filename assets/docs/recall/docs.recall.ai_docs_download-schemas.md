---
url: "https://docs.recall.ai/docs/download-schemas"
title: "Download Schemas"
---

Download URLs are populated once the relevant media object has transitioned to `done` status. For accessing media data during recording, you can use [Real-Time Endpoints](https://docs.recall.ai/docs/real-time-endpoints)

## \[JSON\] Participant Download URL   [Skip link to [JSON] Participant Download URL](https://docs.recall.ai/docs/download-schemas\#json-participant-download-url)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "id": number, // Id of the participant in the meeting. This id is not unique across meetings.\
    "name": string | null, // Display name of the participant.\
    "is_host": boolean | null, // Whether the participant is the host of the meeting.\
    "platform": string | null, // Meeting platform constant\
    "extra_data": json | null, // Extra data about the participant from the meeting platform.\
  }\
]

```

## \[JSON\] Participant Event Download URL   [Skip link to [JSON] Participant Event Download URL](https://docs.recall.ai/docs/download-schemas\#json-participant-event-download-url)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "id": string, // Id of the participant event.\
    "action": string, // The action that the participant took. values: "join" | "leave" | "update" | "speech_on" | "speech_off" | "webcam_on" | "webcam_off" | "screenshare_on" | "screenshare_off" | "chat_message"\
    "participant": {\
      "id": integer, // Id of the participant in the meeting. This id is not unique across meetings.\
      "name": string | null, // Display name of the participant.\
      "is_host": boolean | null, // Whether the participant is the host of the meeting.\
      "platform": string | null, // Meeting platform constant\
      "extra_data": json | null, // Extra data about the participant from the meeting platform.\
    },\
    "timestamp": {\
      "absolute": string, // ISO 8601\
      "relative": number, // seconds\
    },\
    "data":\
    	{\
        "text": string, // The text of chat message\
        "to": string, // The recipient of the chat message. values: "everyone" | "only_bot"\
      } // populated if the action is a `chat_message`\
    	| null\
  }\
]

```

## \[JSON\] Speaker Timeline Download URL   [Skip link to [JSON] Speaker Timeline Download URL](https://docs.recall.ai/docs/download-schemas\#json-speaker-timeline-download-url)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "participant": {\
      "id": integer, // Id of the participant in the meeting. This id is not unique across meetings.\
      "name": string | null, // Display name of the participant.\
      "is_host": boolean | null, // Whether the participant is the host of the meeting.\
      "platform": string | null, // Meeting platform constant\
      "extra_data": json | null, // Extra data about the participant from the meeting platform.\
    },\
    "start_timestamp": {\
      "absolute": string, // ISO 8601\
      "relative": number, // seconds\
    },\
    "end_timestamp": {\
      "absolute": string, // ISO 8601\
      "relative": number, // seconds\
    }\
  }\
]

```

## \[JSON\] Transcript Download URL   [Skip link to [JSON] Transcript Download URL](https://docs.recall.ai/docs/download-schemas\#json-transcript-download-url)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "participant": {\
      "id": number, // Id of the participant in the meeting. This id is not unique across meetings.\
      "name": string | null, // Display name of the participant.\
      "is_host": boolean | null, // Whether the participant is the host of the meeting.\
      "platform": string | null, // Meeting platform constant\
      "extra_data": json | null, // Extra data about the participant from the meeting platform.\
    },\
    "words": [\
      {\
        "text": string, // The text of the word.\
        "start_timestamp": {\
					"absolute": number, // seconds\
          "relative": number // seconds\
        },\
        "end_timestamp": {\
					"absolute": number, // seconds\
          "relative": number // seconds\
        }\
      }\
    ]\
  }\
]

```

## \[JSON\] Participant Separate Video Parts   [Skip link to [JSON] Participant Separate Video Parts](https://docs.recall.ai/docs/download-schemas\#json-participant-separate-video-parts)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "id": string, // Id of the separate part\
    "participant": {\
      "id": integer, // Id of the participant in the meeting. This id is not unique across meetings.\
      "name": string | null, // Display name of the participant.\
      "is_host": boolean | null, // Whether the participant is the host of the meeting.\
      "platform": string | null, // Meeting platform constant\
      "extra_data": json | null, // Extra data about the participant from the meeting platform.\
    },\
    "start_timestamp": {\
      "absolute": string, // ISO 8601\
      "relative": number, // seconds\
    },\
    "duration": number, // seconds\
    "type": "webcam" | "screenshare", // the type of video part\
    "download_url": string, // URL to download the media file from\
  }\
]

```

## \[JSON\] Participant Separate Audio Parts   [Skip link to [JSON] Participant Separate Audio Parts](https://docs.recall.ai/docs/download-schemas\#json-participant-separate-audio-parts)

JSON

```rdmd-code lang-json theme-light

[\
  {\
    "id": string, // Id of the separate part\
    "participant": {\
      "id": integer, // Id of the participant in the meeting. This id is not unique across meetings.\
      "name": string | null, // Display name of the participant.\
      "is_host": boolean | null, // Whether the participant is the host of the meeting.\
      "platform": string | null, // Meeting platform constant\
      "extra_data": json | null, // Extra data about the participant from the meeting platform.\
    },\
    "start_timestamp": {\
      "absolute": string, // ISO 8601\
      "relative": number, // seconds\
    },\
    "duration": number, // seconds\
    "download_url": string, // URL to download the media file from\
  }\
]

```

## \[JSON\] Transcript Provider Data Download URL   [Skip link to [JSON] Transcript Provider Data Download URL](https://docs.recall.ai/docs/download-schemas\#json-transcript-provider-data-download-url)

JSON

```rdmd-code lang-json theme-light

{
  "parts": [\
    {\
      "id": string,\
      "created_at": string, // ISO 8601\
\
      // context of audio which was the transcription source for this part\
      "source_audio": {\
        	"type": "mixed" | "separate",\
          "offset": float, // seconds from recording start\
        	"participant": {\
            "id": integer, // Id of the participant in the meeting. This id is not unique across meetings.\
            "name": string | null, // Display name of the participant.\
            "is_host": boolean | null, // Whether the participant is the host of the meeting.\
            "platform": string | null, // Meeting platform constant\
            "extra_data": json | null, // Extra data about the participant from the meeting platform.\
          } | null  // participant data (only available for type=separate)\
      },\
\
      // part type, dictates the structure of 'data' key\
      "type": "webhook" | "http_response" | "websocket_message",\
      "data":\
      	{ payload: object } // type=webhook,\
        { url: string, status_code: integer, body: object }, // type=http_response\
        { url: string, event: string, payload: object }, // type=websocket_message\
    }\
  ]
}

```

Updated 3 days ago

* * *

Did this page help you?

Yes

No

Ask AI