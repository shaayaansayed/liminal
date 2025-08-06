---
url: "https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms"
title: "Zoom RTMS"
---

> ## 📘  Limitations
>
> - Requires a properly configured Zoom App, which will need to go through [Zoom's application process](https://developers.zoom.us/docs/distribute/app-review-process/)
> - You can only receive data (no sending messages or [Output Media](https://docs.recall.ai/reference/bot_output_media_create))
> - Zoom RTMS doesn't provide chat messages (currently)
> - Zoom RTMS doesn't support Breakout Rooms (currently)

# Zoom Setup   [Skip link to Zoom Setup](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms\#zoom-setup)

01. Make sure you've updated your Zoom client to the latest version

02. Create or edit your [Zoom App](https://marketplace.zoom.us/)

03. In the top right, click Develop -> Build App
    ![](https://files.readme.io/b98856452ac1f0e952398b944bf64e5c9123571a36e3fb562b672b8d1054939e-image.png)

04. Select General App
    ![](https://files.readme.io/48dc83d2af4c6b33b60fa467b9068716adcf31a1a12ae98d6c851f0cb0589fad-image.png)

05. Copy your Client ID and Client Secret
    ![](https://files.readme.io/74b2a802f9e8bdb4f79378127be7f65bac74443fb6b78331488982947f5fac8e-image.png)

06. Click on "Basic Information" (below "Build your app")


    1. Add a OAuth Redirect URL (e.g. [https://my-random-domain.ngrok-free.app/oauth-callback/zoom](https://my-random-domain.ngrok-free.app/oauth-callback/zoom))

![](https://files.readme.io/ab7b664118bfae8e149a696954a9f9243c2e01af73e41c0912135dfcf4ac4541-image.png)

07. Click on "Access" (below "Build your app" and "Features" on the left)

08. Copy your Secret Token
    ![](https://files.readme.io/63f351e5bdcb871e24e4e9fb6418ffb85525c3c261023cdafc17bf900ff57704-image.png)

09. Enable "Event Subscription"
    1. Name the webhook (e.g. My Recall RTMS webhook)
       1. Choose option "Webhook"

       2. Click "Add Events"
          1. ![](https://files.readme.io/3a16ac5315a951b4d12dcfdd95ac731856718af07841185b5bfce7a521749002-image.png)
             Search "RTMS" and select "Select All RTMS"
             1. In "Event notification endpoint URL"


                1. Add the URL where you want to receive a webhook for Zoom RTMS notifications
                2. To get started, we recommend using an [Ngrok static domain](https://dashboard.ngrok.com/domains) followed by /zoom-webhook

                   1. e.g. `https://my-random-domain.ngrok-free.app/zoom-webhook`

![](https://files.readme.io/966cfad6d4a35dc4800307da6e0cca1f174bc727300262e15dba93d6f75d2d35-image.png)

             2. Select "Save"
10. Select "Scopes" (below "Build your app" on the left), then +Add Scopes


    1. Search RTMS
    2. Under "Meeting" enable all the real-time media streams scopes:
       1. meeting:read:meeting\_audio
       2. meeting:read:meeting\_chat
       3. meeting:read:meeting\_transcript
       4. meeting:read:meeting\_screenshare
       5. meeting:read:meeting\_video
    3. Under "RTMS" enable:
       1. rtms:read:rtms\_started
       2. rtms:read:rtms\_stopped

![](https://files.readme.io/2f5d54bda0af4d3ca70ecf24458a2cd6a67d48f7ed7ea93ce5bfe4da1d3cd38f-image.png)

    1. Click "Done"
11. Click "Local Test" (below "Add your App" on the left)
    1. Click "Add App Now"
       ![](https://files.readme.io/2461de9607785edbd01bdaa8894ccb44d50be025996f70a65543d7486ec0f2b4-image.png)

    2. You will see a confirmation prompt, click "Allow"

    3. You will get redirected, the end URL may show an error but that's OK! We now have a Zoom RTMS App!
12. Go to your [Zoom App Settings](https://zoom.us/profile/setting?tab=zoomapps)
    1. Under "Auto-start apps that access shared realtime meeting content" click "Choose an app to auto-start"
       1. In the dropdown select your new app

Your Zoom App is now setup for RTMS!

# Quickstart   [Skip link to Quickstart](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms\#quickstart)

There are multiple ways to connect to a Zoom meeting with RTMS, but we recommend beginning with the auto-start workflow.

Once a meeting starts, Zoom will call the webhook you provided in the Event notification endpoint URL, we'll assume the path is `zoom-webhook`. When Zoom provides a `meeting.rtms_started` event at that endpoint your server must:

- Generate an HMAC signature
- POST the Recall `/api/v1/meeting_direct_connect` endpoint with:

  - The fields that Zoom provided
  - An HMAC signature from your client secret
  - Any additional options consistent with our [Create Bot Endpoint](https://docs.recall.ai/reference/bot_create)

JavaScript

```rdmd-code lang-javascript theme-light

app.post('/zoom-webhook', async (req, res) => {
  const { event, payload } = req.body;

  // Handle URL validation event
  if (event === 'endpoint.url_validation' && payload?.plainToken) {
    // Generate a hash for URL validation using the plainToken and a secret token
    const hash = crypto
      .createHmac('sha256', ZOOM_SECRET_TOKEN)
      .update(payload.plainToken)
      .digest('hex');
    console.log('Responding to URL validation challenge');
    return res.json({
      plainToken: payload.plainToken,
      encryptedToken: hash,
    });
  }

  // Handle RTMS started event
  if (event === 'meeting.rtms_started') {
   await startRecordingRtms(event, payload);
  }

  // Respond with HTTP 200 status
  res.sendStatus(200);
});
async function startRecordingRtms(payload) {
  // Start the recording via Recall
  const { meeting_uuid, rtms_stream_id, server_urls } = payload;
  const response = await fetch(`https://us-east-1.recall.ai/api/v1/meeting_direct_connect`, {
    method: 'POST',
    headers: {
      'Authorization': `Token ${RECALL_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      zoom_rtms: {
        meeting_uuid,
        rtms_stream_id,
        server_urls,
        signature: generateSignature(meeting_uuid, rtms_stream_id)
      },
      // Other options (e.g. recordings, real time events, webhooks, transcriptions)
      // are consistent with https://docs.recall.ai/reference/bot_create
      recording_config: {
        video_mixed_mp4: {}
      }
    })
  });

  const recallRtms = await response.json();

  await saveRecordingToDatabase({
    recallId: recallRtms.id,
    status: recallRtms.status.code,
  });
}
function generateSignature(meetingUuid, streamId) {
  // Create a message string and generate an HMAC SHA256 signature
  const message = `${CLIENT_ID},${meetingUuid},${streamId}`;
  return crypto.createHmac('sha256', CLIENT_SECRET).update(message).digest('hex');
}

```

# Get the Recording   [Skip link to Get the Recording](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms\#get-the-recording)

To get any artifacts from the meeting, you’ll use the id received when creating the meeting\_direct\_connect to query the [Retrieve Meeting Direct Connect](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms) endpoint to receive its current state and any artifacts of recordings or transcriptions

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

# Next Steps   [Skip link to Next Steps](https://docs.recall.ai/docs/meeting-direct-connect-for-zoom-rtms\#next-steps)

- If you want a botless form factor, but without the limitations of Meeting Direct Connect, you should check out the [Desktop SDK](https://docs.recall.ai/docs/desktop-sdk)
- If you want to be able to input chat, audio, or video data into a meeting, check out [Bots](https://docs.recall.ai/docs/bot-overview)

Updated 2 days ago

* * *

- [Google Meet Media API](https://docs.recall.ai/docs/google-meet-media-api)

Did this page help you?

Yes

No

Ask AI