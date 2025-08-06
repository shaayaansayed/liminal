---
url: "https://docs.recall.ai/docs/desktop-sdk"
title: "Desktop SDK"
---

Get meeting recordings and transcripts without a bot \| Recall.ai Desktop Recording SDK Demo - YouTube

[Photo image of Recall](https://www.youtube.com/channel/UCQXsakK2EQOF4qrTsEbyZHg?embeds_widget_referrer=https%3A%2F%2Fdocs.recall.ai%2F&embeds_referring_euri=https%3A%2F%2Fcdn.embedly.com%2F&embeds_referring_origin=https%3A%2F%2Fcdn.embedly.com)

Recall

136 subscribers

[Get meeting recordings and transcripts without a bot \| Recall.ai Desktop Recording SDK Demo](https://www.youtube.com/watch?v=4croAGGiKTA)

Recall

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=4croAGGiKTA&embeds_widget_referrer=https%3A%2F%2Fdocs.recall.ai%2F&embeds_referring_euri=https%3A%2F%2Fcdn.embedly.com%2F&embeds_referring_origin=https%3A%2F%2Fcdn.embedly.com)

0:00

0:00 / 2:04
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=4croAGGiKTA "Watch on YouTube")

The Desktop Recording SDK allows for recording Zoom and Google Meet calls locally, within an Electron application.

Additionally, the Desktop Recording SDK can capture audio for Slack huddles, but currently doesn't capture participant metadata or video for them.

| Meeting Provider | Mac | Windows |
| --- | --- | --- |
| Zoom | ✅ | ✅ |
| Google Meet | ✅ | ❌ |
| Slack | ⚠️ | ❌ |

✅ = Full support

❌ = Not yet supported

⚠️ = Detection support only

The lifecycle of a Desktop Recording SDK recording is as follows:

1. The Desktop Recording SDK notifies your code that a meeting has started locally.
2. Your code makes a request to your backend for an upload token.
3. Your backend [creates a new Desktop SDK Upload using the Recall.ai API](https://docs.recall.ai/docs/desktop-sdk-beta#creating-an-sdk-upload), and returns the upload token to your desktop application.
4. Your desktop code calls `startRecording` with the upload token.
5. Once the meeting is over, call `uploadRecording`.
6. Wait for the `sdk_upload.complete` webhook
7. Run async transcription (optional)
8. Download the recording video and transcription

That's it! Once the call finishes, a recording will be created on the Recall API and your backend will be notified via webhook.

# Installation   [Skip link to Installation](https://docs.recall.ai/docs/desktop-sdk\#installation)

Shell

```rdmd-code lang-shell theme-light

npm install @recallai/desktop-sdk

```

To see how to integrate the SDK with Electron and Webpack, [check out the sample application!](https://github.com/recallai/muesli-public)

For a project you can easily clone and fork to get started without configuring a build system, try one of:

- [Webpack sample](https://github.com/recallai/desktop-sdk-electron-webpack-sample)
- [Vite sample](https://github.com/recallai/desktop-sdk-electron-vite-sample)

> ## 🚧  Note when building for production
>
> By default, Electron Forge's code signing tool, `osx-sign`, has issues signing the Desktop SDK. Recall.ai [provides a fork of `osx-sign`](https://github.com/recallai/osx-sign) you can use to correctly sign the package when you're building your application for release. If you don't want to worry about configuring this, try one of the above sample projects with this already configured!

# Usage   [Skip link to Usage](https://docs.recall.ai/docs/desktop-sdk\#usage)

## `init(config)`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#initconfig)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.init({
  apiUrl: "https://us-east-1.recall.ai",
  acquirePermissionsOnStartup? = ["accessibility", "screen-capture", "microphone"],
  restartOnError = true
});

```

Initialize the Desktop Recording SDK. This should be called once at startup.

- `apiUrl`: The URL corresponding to the region your Recall.ai workspace belongs to.
- `acquirePermissionsOnStartup`: The list of permissions to automatically request when the Desktop Recording SDK initializes. By default, the SDK requests all permissions on initialization.

## `addEventListener(eventType, listener)`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#addeventlistenereventtype-listener)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.addEventListener("permissions-granted", async (evt) => {
  // The user has granted all the required permsisions to start recording
});

RecallAiSdk.addEventListener("meeting-detected", async (evt) => {
  const { window } = evt;
});

RecallAiSdk.addEventListener("sdk-state-change", async (evt) => {
  const {sdk: {state: { code }}} = evt;
  // code is either "recording" or "idle"
});

RecallAiSdk.addEventListener('recording-ended', async (evt) => {
  const { window } = evt;
});

RecallAiSdk.addEventListener('meeting-closed', async (evt) => {
  const { window } = evt;
});

RecallAiSdk.addEventListener('realtime-event', async (evt) => {
  const {window , type, status} = evt;
});

RecallAiSdk.addEventListener('upload-progress', async (evt) => {
  const {
    window: { id },
    progress: progress
  } = evt;
  // Progress is a number from 0-100 representing upload completion
});

RecallAiSdk.addEventListener('recording-started', async (evt) => {
  const { window } = evt;
});

RecallAiSdk.addEventListener('meeting-updated', async (evt) => {
  const { window } = evt;
});

RecallAiSdk.addEventListener('media-capture-status', async (evt) => {
  const { window, type, capturing } = evt;
  // type is 'video' or 'audio'
  // capturing is a boolean indicating capture status
});

RecallAiSdk.addEventListener('participant-capture-status', async (evt) => {
  const { window, type, participantId, capturing } = evt;
  // type is 'video', 'audio', or 'screenshare'
  // capturing is a boolean indicating capture status
});

RecallAiSdk.addEventListener('error', async (evt) => {
  const { window, type, message } = evt;
  const windowId = window?.id;
});

RecallAiSdk.addEventListener('permission-status', async (evt) => {
  const { permission, status } = evt;
  // Permission type (e.g. 'microphone'),
  // status ["granted", "not_requested", "denied"]
  //   (see event listener docs below for more information)
});

RecallAiSdk.addEventListener('shutdown', async (evt) => {
  const { code, signal } = evt;
});

```

Install an event listener for `eventType` events. `eventType` can be one of:

- `permissions-granted`: Triggered when the user has granted all the required permissions to start recording.
- `meeting-detected`: Triggered when a Zoom meeting is found, either when a new one starts, or after the SDK initializes and there is a meeting already in progress.
- `sdk-state-change`: Triggered when the in-progress recording changes state, either to `"idle"` to indicate that recording is over, or `"recording"` to indicate that a recording is in progress.
- `recording-started`: Triggered when a recording has started.
- `recording-ended`: Triggered when a recording has stopped, due to the meeting ending, or calling `stopRecording`.
- `meeting-closed`: Triggered when a detected meeting has ended.
- `media-capture-status`: Triggered when media capture has been interrupted or resumed. In some cases, the meeting window can't be captured, so only audio is received (for instance, when the meeting window is on an inactive virtual desktop).
- `realtime-event`: Triggered when real-time data is available, such as transcript information or participant join/leave events. Subscribe to real-time events with `startRecording` to receive these callbacks.
- `upload-progress`: Triggered to notify your code of the state of a video upload. `progress` is a number from 0 to 100 representing upload completion.
- `meeting-updated`: Triggered when meeting information has updated (usually when `title` or `url` have become known)
- `error`: Triggered when the Desktop Recording SDK has encountered an error. Right now, the only type is `process`, which indicates that the SDK has exited unexpectedly or failed to start. The SDK automatically tries to restart in case of unexpected shutdown, so it's not necessary to initialize and set up callbacks again.
- `permission-status`: Triggered on startup to indicate the current status of the required permissions. The permission will be one of `accessibility`, `screen-capture`, or `microphone`. Status will be one of:

  - `granted` \- Indicates that the permission was successfully granted.
  - `not_requested` \- A soft failure; the user has not yet been prompted for permission. The SDK is expected to display the permission dialog shortly.
  - `denied` \- A hard failure; the end user has explicitly denied the permission request.
- `shutdown`: Triggered when the the Desktop Recording SDK shuts down normally.


## `startRecording({windowId, uploadToken})`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#startrecordingwindowid-uploadtoken)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.startRecording({
  windowId: ...,
  uploadToken: ...
});

```

Begin recording. This function is usually called inside an event listener for `meeting-detected`. `windowId` is provided by the `meeting-detected` callback, and `uploadToken` is acquired by creating an SDK Upload on your backend.

See [Real-Time Event Payloads](https://docs.recall.ai/docs/real-time-event-payloads#participant_events) for more details on the schema of the data.

## `stopRecording({windowId})`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#stoprecordingwindowid)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.stopRecording({
  windowId: ...,
});

```

Stop recording. This function can be called to end a recording before the meeting itself has naturally ended.

## `pauseRecording({windowId})`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#pauserecordingwindowid)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.pauseRecording({
  windowId: ...,
});

```

Pause recording. This will make cause the resulting video or audio to be blank for the duration of the paused period.

## `resumeRecording({windowId})`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#resumerecordingwindowid)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.resumeRecording({
  windowId: ...,
});

```

Resume recording.

## `uploadRecording({windowId})`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#uploadrecordingwindowid)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.uploadRecording({
  windowId: ...
});

```

Initiate the upload of a recording. This function should be called only after a recording has completed, usually in a `recording-ended` callback.

## `prepareDesktopAudioRecording()`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#preparedesktopaudiorecording)

JavaScript

```rdmd-code lang-javascript theme-light

import RecallAiSdk from '@recallai/desktop-sdk';

const res = await Backend.fetch(`/api/create_sdk_recording`, AppState.client_token);
const payload = await res.json();
const windowId = await RecallAiSdk.prepareDesktopAudioRecording();

await RecallAiSdk.startRecording({
  windowId,
  uploadToken: res.upload_token
});

```

In addition to recording Zoom meetings, the Desktop Recording SDK can also record whole-desktop audio. This can be used to implement, for example, realtime note-takers for in person meetings or for platforms not yet supported by the Desktop Recording SDK.

## `requestPermission(permission)`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#requestpermissionpermission)

JavaScript

```rdmd-code lang-javascript theme-light

let permission = ...; // one of `accessibility`, `screen-capture`, or `microphone`.
RecallAiSdk.requestPermission(permission);

```

If the Desktop Recording SDK is initialized to not request permissions on startup, you can manually request a permission using `requestPermission`. This will cause a dialog box to be presented to the user if the permission hasn't been requested before. If it has been declined before, nothing will happen.

## `shutdown()`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#shutdown)

JavaScript

```rdmd-code lang-javascript theme-light

RecallAiSdk.shutdown();

```

Shuts down the SDK. After calling this function, to resume use, the SDK must be initialized using `init()` again.

# Creating an SDK upload   [Skip link to Creating an SDK upload](https://docs.recall.ai/docs/desktop-sdk\#creating-an-sdk-upload)

Create an SDK upload using the [Create Desktop SDK Upload](https://docs.recall.ai/reference/sdk_upload_create) endpoint. This endpoint is similar to `Create Bot`, and it is here that you can configure the captured data and specify what realtime events you want to receive.

#### Request   [Skip link to Request](https://docs.recall.ai/docs/desktop-sdk\#request)

You can just make a POST request to get the defaults (video and participant events).

Python

```rdmd-code lang-Text theme-light

requests.post(
    f"{settings.RECALLAI_API_BASE}/api/v1/sdk-upload/",
    headers={"Authorization": f"Token {api_key}"},
)

```

You can also specify a transcript provider to receive transcript events during the recording. Currently, `assembly_ai_streaming` and `deepgram_streaming` are supported, and we are actively working on supporting other providers.

Note that when using `deepgram_streaming`, your API token in the Recall dashboard must have the the `keys:write` permission, and you must specify a [Project ID.](https://developers.deepgram.com/guides/deep-dives/managing-projects)

Python

```rdmd-code lang-python theme-light

requests.post(
    f"{settings.RECALLAI_API_BASE}/api/v1/sdk-upload/",
    headers={"Authorization": f"Token {api_key}"},
    json={
        "transcript": {
            "provider": {
                "assembly_ai_streaming": {}
            }
        }
    }
)

```

#### Response   [Skip link to Response](https://docs.recall.ai/docs/desktop-sdk\#response)

json

```rdmd-code lang-json theme-light

{
   "id": "4abf29fc-36b5-4853-9f84-a9990b9e354b",
   "upload_token": "96472e47-a78c-4774-a9a2-9349327d398d"
}

```

# Example   [Skip link to Example](https://docs.recall.ai/docs/desktop-sdk\#example)

This is a minimal example demonstrating how to use these functions together:

JavaScript

```rdmd-code lang-javascript theme-light

import RecallAiSdk from '@recallai/desktop-sdk';

RecallAiSdk.init({
  api_url: "https://us-east-1.recall.ai"
});

RecallAiSdk.addEventListener('meeting-detected', async (evt) => {
  const res = await Backend.fetch(`/api/create_sdk_recording`, AppState.client_token);
  const payload = await res.json();

  await RecallAiSdk.startRecording({
    windowId: evt.window.id,
    uploadToken: res.upload_token
  });
});

RecallAiSdk.addEventListener('sdk-state-change', async (evt) => {
  switch (evt.sdk.state.code) {
    case 'recording':
      console.log("SDK is recording");
      break;
    case 'idle':
      console.log("SDK is idle");
      break;
  }
});

RecallAiSdk.addEventListener('recording-ended', async (evt) => {
  RecallAiSdk.uploadRecording({ windowId: evt.window.id });
});

RecallAiSdk.addEventListener('upload-progress', async (evt) => {
  console.log(`Uploaded ${evt.progress}%`);
});

```

# Webhooks   [Skip link to Webhooks](https://docs.recall.ai/docs/desktop-sdk\#webhooks)

At points in the lifecycle of a Desktop SDK Upload, you will receive webhook notifications about the state of the upload. Webhooks are sent through Svix and can be configured in your [Recall dashboard](https://api.recall.ai/dashboard/webhooks/).

## `sdk_upload.complete`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#sdk_uploadcomplete)

This webhook is sent when an SDK Upload has finished successfully.

Webhook Payload

```rdmd-code lang-json theme-light

{
  "data": {
    "data": {
      "code": "complete",
      "sub_code": null,
      "updated_at": "2025-05-10T15:48:24.034072Z"
    },
    "recording": {
      "id": "0206f11b-68ab-42b1-8a30-b85f60076e83",
      "metadata": {}
    },
    "sdk_upload": {
      "id": "fa08e580-d7b6-4f88-9f71-5b718c5a5f77",
      "metadata": {}
    }
  },
  "event": "sdk_upload.complete"
}

```

## `sdk_upload.failed`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#sdk_uploadfailed)

This webhook is sent when an SDK Upload has finished unsuccessfully.

Webhook Payload

```rdmd-code lang-json theme-light

{
  "data": {
    "data": {
      "code": "failed",
      "sub_code": null,
      "updated_at": "2025-05-10T15:48:24.034072Z"
    },
    "recording": {
      "id": "0206f11b-68ab-42b1-8a30-b85f60076e83",
      "metadata": {}
    },
    "sdk_upload": {
      "id": "fa08e580-d7b6-4f88-9f71-5b718c5a5f77",
      "metadata": {}
    }
  },
  "event": "sdk_upload.failed"
}

```

## `sdk_upload.uploading`   [Skip link to [object Object]](https://docs.recall.ai/docs/desktop-sdk\#sdk_uploaduploading)

This webhook is sent when the SDK upload has started uploading to the Recall.ai platform.

Webhook Payload

```rdmd-code lang-json theme-light

{
  "data": {
    "data": {
      "code": "uploading",
      "sub_code": null,
      "updated_at": "2025-05-10T15:48:24.034072Z"
    },
    "recording": {
      "id": "0206f11b-68ab-42b1-8a30-b85f60076e83",
      "metadata": {}
    },
    "sdk_upload": {
      "id": "fa08e580-d7b6-4f88-9f71-5b718c5a5f77",
      "metadata": {}
    }
  },
  "event": "sdk_upload.uploading"
}

```

# Running transcription   [Skip link to Running transcription](https://docs.recall.ai/docs/desktop-sdk\#running-transcription)

| Provider | Suported |
| --- | --- |
| `assembly_ai_streaming` | ✅ |
| `deepgram_streaming` | ✅ |

After receiving the `sdk_upload.complete` webhook you can retrieve the recorded video file using create transcript artifact endpoint with the `recording_id` field from the webhook:

#### Endpoint   [Skip link to Endpoint](https://docs.recall.ai/docs/desktop-sdk\#endpoint)

Shell

```rdmd-code lang-shell theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/recording/71f4d556-4c8c-4627-a253-61344e8f22f7/create_transcript \
     --header 'Authorization: Token your-recall-api-token' \
     --header 'content-type: application/json' \
     --data '{
        "provider": {
            "assembly_ai_async": {
                "language_code": "en"
            }
        },
        "diarization": {
            "algorithm_priority": ["speaker_timeline"]
        }
    }'

```

#### Response   [Skip link to Response](https://docs.recall.ai/docs/desktop-sdk\#response-1)

JSON

```rdmd-code lang-json theme-light

{
  "id": "642a12e1-c542-4c27-80be-ea67f41d3196,
  "status": {
    "code": "processing"
  }
}

```

# Retrieve the recording & transcript   [Skip link to Retrieve the recording & transcript](https://docs.recall.ai/docs/desktop-sdk\#retrieve-the-recording--transcript)

After receiving the `sdk_upload.complete` webhook you can retrieve the recorded video file using retrieve recording endpoint with the `recording_id` field from the webhook:

#### Endpoint   [Skip link to Endpoint](https://docs.recall.ai/docs/desktop-sdk\#endpoint-1)

Shell

```rdmd-code lang-shell theme-light

curl --request GET \
     --url https://us-east-1.recall.ai/api/v1/recording/71f4d556-4c8c-4627-a253-61344e8f22f7 \
     --header 'Authorization: Token your-recall-api-token' \
     --header 'content-type: application/json'

```

#### Response   [Skip link to Response](https://docs.recall.ai/docs/desktop-sdk\#response-2)

JSON

```rdmd-code lang-json theme-light

{
  "id": "71f4d556-4c8c-4627-a253-61344e8f22f7",
  "media_shortcuts": {
    "video_mixed": {
      "status": {
        "code": "done"
      },
      "data": {
        "download_url": "https://some-download-endpoint",
      }
    },
    "transcript": {
      "status": {
        "code": "done"
      },
      "data": {
        "download_url": "https://some-download-endpoint",
      }
    }
  }
}

```

# FAQs   [Skip link to FAQs](https://docs.recall.ai/docs/desktop-sdk\#faqs)

### How does the Desktop Recording SDK stay compliant with recording laws?   [Skip link to How does the Desktop Recording SDK stay compliant with recording laws?](https://docs.recall.ai/docs/desktop-sdk\#how-does-the-desktop-recording-sdk-stay-compliant-with-recording-laws)

The developer is responsible for staying compliant with recording laws, and Recall only provides the tools to enable recording on desktop.

Updated 3 days ago

* * *

Did this page help you?

Yes

No

Ask AI