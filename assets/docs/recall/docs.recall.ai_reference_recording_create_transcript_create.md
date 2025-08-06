---
url: "https://docs.recall.ai/reference/recording_create_transcript_create"
title: "Create Async Transcript"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Retrieving recent requests… |

LoadingLoading…

#### URL Expired

The URL for this request expired after 30 days.

> ## 📘  Notice on Transcription Options
>
> Starting July 2025, new customers will use an updated transcription system that directly passes request bodies to providers, as outlined in the documentation below. Existing customers on the older system without this feature can opt in by contacting customer support.

id

uuid

required

A UUID string identifying this recording.

metadata

object

metadata object

provider

object

required

provider object

# `` 200

Updated 12 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Base URL

https://us-east-1.recall.ai/api/v1/recording/{id}/create\_transcript/

```

xxxxxxxxxx

31

1curl --request POST \

2     --url https://us-east-1.recall.ai/api/v1/recording/id/create_transcript/ \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "provider": {

8    "gladia_v2_async": {

9      "subtitles_config": {

10        "formats": [\
\
11          "srt"\
\
12        ]

13      },

14      "translation_config": {

15        "target_languages": [\
\
16          "af"\
\
17        ]

18      }

19    },

20    "rev_async": {

21      "translation_config": {

22        "target_languages": [\
\
23          {\
\
24            "model": 0\
\
25          }\
\
26        ]

27      }

28    }

29  }

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200

Updated 12 days ago

* * *

Did this page help you?

Yes

No