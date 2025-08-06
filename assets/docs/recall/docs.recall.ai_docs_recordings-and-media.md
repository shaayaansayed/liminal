---
url: "https://docs.recall.ai/docs/recordings-and-media"
title: "Recordings and Media"
---

# Recordings   [Skip link to Recordings](https://docs.recall.ai/docs/recordings-and-media\#recordings)

Recordings are the fundamental entity for capturing and storing conversation data.

A recording serves as a container that encapsulates various types of conversation data and metadata, providing both real-time data streams through [Real-Time Endpoints](https://docs.recall.ai/docs/real-time-endpoints) and comprehensive snapshots of meetings or interactions through Media objects.

Recordings can be generated through a variety of data sources, such a [Meeting Bots](https://docs.recall.ai/docs/bot-overview) and the [Desktop SDK](https://docs.recall.ai/docs/desktop-sdk-beta).

# Media   [Skip link to Media](https://docs.recall.ai/docs/recordings-and-media\#media)

Media refers to the different types of data produced by a recording. Each captures a distinct aspect of the conversation, enabling targeted use cases such as transcription analysis, participant behavior tracking, or meeting playback.

Media object expose the data captured by them through the `data` field including [download urls](https://docs.recall.ai/docs/download-urls) for various cases. These are available once a media object is complete (i.e it has transitioned to the `done` status).

Some examples can be found below.

## **Transcript**   [Skip link to [object Object]](https://docs.recall.ai/docs/recordings-and-media\#transcript)

Provides the text representation of the conversation, including who said what and when. Transcripts can be used for searching, analyzing, or summarizing the conversation content.

_See: [Generating Transcripts](https://docs.recall.ai/docs/real-time-vs-async-transcription)_

## **Video (Mixed)**   [Skip link to [object Object]](https://docs.recall.ai/docs/recordings-and-media\#video-mixed)

Mixed video refers to a single video file containing all participants’ video feeds combined into one stream. Ideal for replaying the entire meeting as it happened.

_See: [Bot Recording](https://docs.recall.ai/docs/receive-a-recording)_

## **Audio (Mixed)**   [Skip link to [object Object]](https://docs.recall.ai/docs/recordings-and-media\#audio-mixed)

Mixed audio refers to a single audio file containing all participants' audio feeds combined into one stream. Ideal for replaying the conversation's audio and generating transcripts.

## **Participant Events**   [Skip link to [object Object]](https://docs.recall.ai/docs/recordings-and-media\#participant-events)

A detailed log of participant activities during the meeting, such as join/leave times, active speaker events, and other engagement actions. Useful for analyzing participant behavior and engagement patterns.

_See: [Participants Events](https://docs.recall.ai/docs/meeting-participants-events)_

## **Meeting Metadata**   [Skip link to [object Object]](https://docs.recall.ai/docs/recordings-and-media\#meeting-metadata)

Structured data that includes key information about the meeting, such as the meeting title or unique identifiers (though importantly, the metadata exposed by a given meeting platform varies). Useful for providing high-level information about a given meeting.

_See: [Meeting Metadata](https://docs.recall.ai/docs/meeting-metadata)_

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI