---
url: "https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api"
title: "Google Meet Media API"
---

> ## 📘  Limitations
>
> - Currently, because this feature is still in preview mode, all meeting participants need to be enrolled in Google's [developer program](https://docs.google.com/forms/d/e/1FAIpQLSd7BiMXXHDlUDkF7G0TSY5zfJbQwFNH3m6K_ZYFi3vCHLFbng/viewform?resourcekey=0-1uHeVg8junj3PPTLNcn7WQ)
> - Google's Meet Media API only sends audio and video of the 3 most relevant participants at any given time
> - You can only receive media data (no sending messages or [Output Media](https://docs.recall.ai/reference/bot_output_media_create))
> - Meet Media does not support Breakout rooms
> - Meet Media API doesn’t send out transcriptions of the meeting, so instead of requesting [meeting\_captions](https://docs.recall.ai/docs/meeting-caption-transcription) you’ll need to use one of our [Transcription Providers](https://docs.recall.ai/docs/ai-transcription)

# Google Cloud Setup   [Skip link to Google Cloud Setup](https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api\#google-cloud-setup)

1. Access or create a Google Cloud Account
2. Join Google Cloud Developer Program
1. Current **all** participants need to be in Google's [Developer Program](https://docs.google.com/forms/d/e/1FAIpQLSd7BiMXXHDlUDkF7G0TSY5zfJbQwFNH3m6K_ZYFi3vCHLFbng/viewform?resourcekey=0-1uHeVg8junj3PPTLNcn7WQ) in order to use Meeting Direct Connect
3. Create a [Google Client ID](https://console.developers.google.com/auth/clients)
1. Select "Web Application"
2. Add an Authorized JavaScript origin with your domain
      1. We recommend testing with an [Ngrok static domain](https://dashboard.ngrok.com/domains) to get started
3. Save this Client ID
4. Enable the [Google Meet API](https://console.cloud.google.com/apis/library/meet.googleapis.com)

# Quickstart   [Skip link to Quickstart](https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api\#quickstart)

Before you connect to a Google Meet, you'll need a way to [generate an OAuth token](https://developers.google.com/identity/oauth2/web/guides/use-token-model) from your Google Cloud ClientID.

JavaScript

```rdmd-code lang-javascript theme-light

const client = google.accounts.oauth2.initTokenClient({
  client_id: clientId,
  scope: 'https://www.googleapis.com/auth/meetings.space.created https://www.googleapis.com/auth/meetings.conference.media.readonly https://www.googleapis.com/auth/meetings.space.readonly',
  callback: (tokenResponse) => {
    console.log(tokenResponse.access_token);
    window.accessToken = tokenResponse.access_token;
  },
  error_callback: (errorResponse) => {
    console.log('error');
    console.log(errorResponse);
  },
});
window.client = client;
client.requestAccessToken();

```

Once you've generated your temporary OAuth `access_token` start the meeting and get the `space_name`. This is the 12 character path after `meet.google.com/`

JavaScript

```rdmd-code lang-javascript theme-light

const response = await fetch(`https://us-east-1.recall.ai/api/v1/meeting_direct_connect`, {
  method: 'POST',
  headers: {
    'Authorization': `Token ${RECALL_API_KEY}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    google_meet_media_api: {
      space_name: $SPACE_NAME,
      access_token: window.accessToken
    },
    // Other options (e.g. recordings, real time events, webhooks, transcriptions)
    // are consistent with https://docs.recall.ai/reference/bot_create
    // NOTE meeting_captions (https://docs.recall.ai/docs/meeting-caption-transcription) won’t work with Meet Media, as only audio and video streams are output
    // If you want transcriptions with Google Meet Media API, please use a transcription provider: https://docs.recall.ai/docs/ai-transcription
    recording_config: {
      video_mixed_mp4: {}
    }
  })
});

```

# Get the Recording   [Skip link to Get the Recording](https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api\#get-the-recording)

To get any artifacts from the meeting, you’ll use the id received when creating the meeting\_direct\_connect to query the [Retrieve Meeting Direct Connect](https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api) endpoint to receive its current state and any artifacts of recordings or transcriptions

JavaScript

```rdmd-code lang-javascript theme-light

const meetingObj = await fetch(`https://us-east-1.recall.ai/api/v1/meeting_direct_connect/${my_mdc_id}`, {
  headers: {
    'Authorization': `Token ${RECALL_API_KEY}`
  }
}).then(r => r.json());

```

This object will contain a recordings section with pre-signed links to view your Meeting Direct Connect recordings

JavaScript

```rdmd-code lang-javascript theme-light

if (meetingObj.recordings.length == 0) {
  console.log("No recordings were made, maybe you didn’t request one?");
} else {
  var videoLink = meetingObj.recordings[0].media_shortcuts.data.download_url;
  console.log(`Your recording is ready to view at ${videoLink}`);
}

```

# Next Steps   [Skip link to Next Steps](https://docs.recall.ai/docs/meeting-direct-connect-for-google-meet-media-api\#next-steps)

- If you want a botless form factor, but without the limitations of Meeting Direct Connect, you should check out the [Desktop SDK](https://docs.recall.ai/docs/desktop-sdk)
- If you want to be able to input chat, audio, or video data into a meeting, check out [Bots](https://docs.recall.ai/docs/bot-overview)

Updated 3 days ago

* * *

- [Zoom RTMS](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms)

Did this page help you?

Yes

No

Ask AI