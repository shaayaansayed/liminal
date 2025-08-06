---
url: "https://docs.recall.ai/docs/bot-detection"
title: "Bot Detection"
---

Recall provides multiple ways to mitigate instances of meetings where participants are bots leading to longer recording lengths and processing times. There are various heuristics that can be enabled/configured depending on usage pattern and requirements.

### Using Silence Detection   [Skip link to Using Silence Detection](https://docs.recall.ai/docs/bot-detection\#using-silence-detection)

This heuristic uses period of continuous silence in a call to detect if there are only bots remaining in the call.

- `automatic_leave.silence_detection.timeout`: The number of seconds of continuous silence that should occur on the call for the bot to automatically leave. ( **Default: 3600(60 minutes)**)
- `automatic_leave.silence_detection.activate_after`: In some cases meeting can start late which can cause continuous silence at the beginning (when bots join on time). You can use this parameter to avoid such false positives by adding a buffer before silence detection is activated. ( **Default: 1200(20 minutes)**)

### Using Participant Names   [Skip link to Using Participant Names](https://docs.recall.ai/docs/bot-detection\#using-participant-names)

This heuristic relies on marking participants as bots based of their name in the meeting.

- `automatic_leave.bot_detection.using_participant_names.matches`: Provide a list of strings which will be substring matched (case insensitively) to every participant name to mark them as a bot. For e.g given `matches: ['notetaker']`, a participant with name `Meeting Notetaker` will be marked as a bot.
- `automatic_leave.bot_detection.using_participant_names.timeout`: The number of seconds after which the bot will leave the call if all remaining participants have been marked as bots
- `automatic_leave.bot_detection.using_participant_names.activate_after`: Similar to previous heuristic, this parameter can be used to add a buffer before the heuristic gets activated to avoid false positives.

### Using Participant Events   [Skip link to Using Participant Events](https://docs.recall.ai/docs/bot-detection\#using-participant-events)

This heuristic relies on marking participants as bots based on their activity in the call. A participant who has not emitted either `active_speaker` or `screenshare_start` for the entire duration of the meeting is marked as a bot.

- `automatic_leave.bot_detection.using_participant_events.timeout`: The number of seconds after which the bot will leave the call if all remaining participants have been marked as bots. ( **Default: 600(10 minutes)**)
- `automatic_leave.bot_detection.using_participant_events.activate_after`: Similar to previous heuristic, this parameter can be used to add a buffer before the heuristic gets activated to avoid false positives. ( **Default: 1200(20 minutes)**)

_Participant events are generally less reliable than participant names as a heuristic for detecting bots. If your bot names use identifiable phrases such as 'bot', 'notetaker', or your company name, we highly recommend using this for best bot detection accuracy._

Updated about 1 year ago

* * *

Did this page help you?

Yes

No

Ask AI