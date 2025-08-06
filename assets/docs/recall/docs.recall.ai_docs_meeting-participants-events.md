---
url: "https://docs.recall.ai/docs/meeting-participants-events"
title: "Meeting Participants & Events"
---

Most recordings typically have associated meeting participants and participant events. Recall.ai's API exposes these through a variety of endpoints outlined below.

# Participants   [Skip link to Participants](https://docs.recall.ai/docs/meeting-participants-events\#participants)

* * *

Recall.ai records and exposes participants for recordings automatically, so no configuration is needed.

## Retrieving Participants   [Skip link to Retrieving Participants](https://docs.recall.ai/docs/meeting-participants-events\#retrieving-participants)

The response schema can be found at [Participants Download Schema](https://docs.recall.ai/docs/download-urls#json-participant-download-url).

### Retrieve participants for a bot   [Skip link to Retrieve participants for a bot](https://docs.recall.ai/docs/meeting-participants-events\#retrieve-participants-for-a-bot)

After calling the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) endpoint, the `recordings` in the response will contain a `media_shortcuts` object.

In this object, you can download the participants by accessing the `participant_events.data.participants_download_url`:

```rdmd-code lang- theme-light
{
  "recordings": [\
    {\
      "id": "a5437136-4b69-429a-9e0c-cd388fd8fee6",\
      ...\
      "participant_events": {\
        "id": "a7ae9238-0e2d-40f2-8480-8e9c0cf3af6c",\
        "data": {\
          "participants_download_url": "https://us-east-1.recall.ai/api/v1/download/participants?token=eyJpZCI6ImE3YWU5MjM4LTBlMmQtNDBmMi04NDgwLThlOWMwY2YzYWY2YyJ9%3A1tOqjv%3AapjfmYtSltJrroNgtl0RORSrwP-Q03ErOq7VymGbwuY",\
          ...\
        }\
      },\
    }\
  ],
  ...
]

```

### Retrieve participants for a recording   [Skip link to Retrieve participants for a recording](https://docs.recall.ai/docs/meeting-participants-events\#retrieve-participants-for-a-recording)

To retrieve a given recording's list of participants, you can call the [List Participant Events](https://docs.recall.ai/reference/participant_events_list) endpoint, using the bot's corresponding recording ID:

cURL

```rdmd-code lang-curl theme-light

curl --request GET \
     --url https://us-east-1.recall.ai/api/v1/participant_events?recording_id=RECORDING_ID \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json"

```

_Example Response:_

JSON

```rdmd-code lang-json theme-light

{
  "next": "...", // URL pre-filled with params/cursor value to fetch the next page
  "previous": "...",
  "results": [\
    {\
      id: "...",\
      // ...\
      data: {\
	      participant_events_download_url: '...',\
				speaker_timeline_download_url: '...',\
				participants_download_url: '...'\
      }\
    }\
  ]
}

```

Then you can query the `participants_download_url` and you will receive the data in JSON format as seen in [this schema](https://docs.recall.ai/docs/download-schemas#json-participant-download-url)

# Participant Events   [Skip link to Participant Events](https://docs.recall.ai/docs/meeting-participants-events\#participant-events)

* * *

Recall.ai exposes participant events as an artifact of a recording.

## Configuration   [Skip link to Configuration](https://docs.recall.ai/docs/meeting-participants-events\#configuration)

To configure a bot to record participant events, no configuration is needed, since the default is to generate this artifact.

You can also explicitly set this by providing an `participant_events` object in your [Create Bot](https://docs.recall.ai/reference/bot_create) request's `recording_config`:

CSS

```rdmd-code lang-css theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
		 --header "authorization: $RECALLAI_API_KEY"
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "meeting_url": "https://meet.google.com/ggt-kpdk-mrj",
  "recording_config": {
    "participant_events": {}
  }
}
'

```

## Retrieving Events   [Skip link to Retrieving Events](https://docs.recall.ai/docs/meeting-participants-events\#retrieving-events)

To retrieve a bot's participant events, you can call the [Retrieve Bot](https://docs.recall.ai/reference/bot_retrieve) and access the `media_shorcuts.participant_events.data.participant_events_download_url` in the recording object.

The response schema can be found [Download URL Schemas: Participant Events](https://docs.recall.ai/docs/download-urls#json-participant-event-download-url).

To retrieve all participant events for a specific **recording**, use the [List Participant Events](https://docs.recall.ai/reference/participant_events_list) endpoint while specifying a `recording_id`:

```rdmd-code lang- theme-light
curl --request GET \
     --url 'https://us-east-1.recall.ai/api/v1/participant_events/?recording_id={RECORDING_ID}' \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json"

```

_Example response_

JSON

```rdmd-code lang-json theme-light

{
  "next": "...",
  "previous": "...",
  "results": [\
    {\
      "id": "9aa74189-92d0-410a-b247-4239e42c2465",\
      "recording_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",\
      "created_at": "2024-12-01T21:29:51.019Z",\
      "status": {\
        "code": "string",\
        "sub_code": "string",\
        "updated_at": "2024-12-01T21:29:51.019Z"\
      },\
      "metadata": {},\
      "data": {\
        "participant_events_download_url": "https://...",\
        "speaker_timeline_download_url": "https://...",\
        "participants_download_url": "https://..."\
      }\
    }\
  ]
}

```

The `data.download_url` will be populated with a pre-signed URL where you can download the entire artifact's contents.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/meeting-participants-events\#faq)

* * *

## Can I get participant emails from the bot?   [Skip link to Can I get participant emails from the bot?](https://docs.recall.ai/docs/meeting-participants-events\#can-i-get-participant-emails-from-the-bot)

Meeting platforms don't expose participant emails for security reasons, so bots aren't able to capture participant emails just by being present in the call.

To map participants to their corresponding email addresses, you can use the [Recall Calendar Integration](https://docs.recall.ai/docs/calendar-integration), or implement a calendar integration of your own.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI