---
url: "https://docs.recall.ai/docs/native-bots"
title: "Native Bots (Zoom)"
---

Bots come in two varieties: **Native** and **Web**.

**Web bots:** The default meeting bot. Recommended for a vast majority of use cases.

**Native bots:** A distinct type of bot that enables native-specific features specifically for Zoom. Only for a small minority of use cases.

Web bots are enabled by default and typically work well for most use cases. If your application requires Native bot features, such as separate audio streams, this guide will help you get up and running with Native bots.

# How to configure native bots   [Skip link to How to configure native bots](https://docs.recall.ai/docs/native-bots\#how-to-configure-native-bots)

You can configure a Zoom Native bot through the `variant` parameter in your [Create Bot](https://docs.recall.ai/reference/bot_create) request:

cURL

```rdmd-code lang-curl theme-light

curl --request POST \
     --url https://us-east-1.recall.ai/api/v1/bot/ \
     --header "Authorization: $RECALLAI_API_KEY" \
     --header "accept: application/json" \
     --header "content-type: application/json" \
     --data '
{
  "meeting_url": "https://zoom.us/j/123456789",
  "variant": {
    "zoom": "native"
  }
}
'

```

# Limitations   [Skip link to Limitations](https://docs.recall.ai/docs/native-bots\#limitations)

Currently Zoom Native bots have the following limitations:

- Cannot [Output Audio](https://docs.recall.ai/reference/bot_output_audio_create)
- Cannot [Receive Chat Messages](https://docs.recall.ai/docs/receiving-chat-messages)
- Cannot [Output Media](https://docs.recall.ai/reference/bot_output_media_create)
- Cannot receive audio from dialed-in participants\*

_\*Limitation of Zoom Meeting SDK for Linux_

Updated 11 days ago

* * *

Did this page help you?

Yes

No

Ask AI