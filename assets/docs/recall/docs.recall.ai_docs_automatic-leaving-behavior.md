---
url: "https://docs.recall.ai/docs/automatic-leaving-behavior"
title: "Automatic Leaving Behavior"
---

There are certain scenarios where you might want your bot to automatically leave calls.

Some of these include:

1. When a bot is stuck in a waiting room
2. When everyone leaves the call
3. When there are only other bots left in the call
4. When a bot is in a call but not recording.

# **Default Values**   [Skip link to [object Object]](https://docs.recall.ai/docs/automatic-leaving-behavior\#default-values)

To control the behavior of bots leaving calls, you can configure the `automatic_leave` object when calling [Create Bot](https://docs.recall.ai/reference/bot_create).

Recall automatically sets sensible defaults when a parameter isn't provided. The defaults (in seconds) for are as follows:

JSON

```rdmd-code lang-json theme-light

automatic_leave: {
  silence_detection: {
    timeout: 3600,
    activate_after: 1200
  },
  bot_detection: {
    using_participant_events: {
      timeout: 600,
      activate_after: 1200
    },
    using_participant_names: {
      timeout: 3600,
      activate_after: 1200
    }
  },
  waiting_room_timeout: 1200,
  noone_joined_timeout: 1200,
  everyone_left_timeout: 2,
  in_call_not_recording_timeout: 3600,
  recording_permission_denied_timeout: 30
}

```

# **Waiting Room Timeout**   [Skip link to [object Object]](https://docs.recall.ai/docs/automatic-leaving-behavior\#waiting-room-timeout)

* * *

You can use the `automatic_leave.waiting_room_timeout` parameter to customize the timeout of bots in waiting rooms.

For timeouts triggered by the `automatic_leave.waiting_room_timeout` parameter, the bot status change will contain a `timeout_exceeded_waiting_room` sub code.

The default value is 20 minutes (1200 seconds), but keep in mind that there are also _platform-specific_ considerations for waiting rooms, namely, for Google Meet.

**Platform Waiting Rooms**

| Platform | Default Timeout | Can disable? |
| --- | --- | --- |
| Google Meet | 10 minutes | ❌ |
| Microsoft Teams | 30 minutes | ❌ |
| Zoom | Indefinite | ✅ |

## Platform default timeouts   [Skip link to Platform default timeouts](https://docs.recall.ai/docs/automatic-leaving-behavior\#platform-default-timeouts)

While there is no timeout for Zoom and Microsoft Teams, Google Meet has a built-in timeout of 10 minutes.

This means that even if you set the bot waiting room timeout to 15 minutes, they will timeout after 10 minutes of being in a Google Meet waiting room.

If a bot times out due to platform timeout, the bot status change will contain a `call_ended_by_platform_waiting_room_timeout` sub code.

## Disabled waiting rooms   [Skip link to Disabled waiting rooms](https://docs.recall.ai/docs/automatic-leaving-behavior\#disabled-waiting-rooms)

The other thing to keep in mind is that for some platforms, hosts can **disable waiting rooms**.

Think about the bot just like a normal participant. If there's a waiting room enabled, then it will go into the waiting room with other participants.

If there is no waiting room enabled, then it will skip the waiting room and join the meeting directly, just like other participants.

# **Bot Detection**   [Skip link to [object Object]](https://docs.recall.ai/docs/automatic-leaving-behavior\#bot-detection)

* * *

Recall provides multiple ways to mitigate instances of meetings where participants are bots leading to longer recording lengths and processing times. There are various heuristics that can be enabled/configured depending on usage pattern and requirements.

## Using Silence Detection   [Skip link to Using Silence Detection](https://docs.recall.ai/docs/automatic-leaving-behavior\#using-silence-detection)

This heuristic uses period of continuous silence in a call to detect if there are only bots remaining in the call.

- `automatic_leave.silence_detection.timeout`: The number of seconds of continuous silence that should occur on the call for the bot to automatically leave. ( **Default: 3600(60 minutes)**)
- `automatic_leave.silence_detection.activate_after`: In some cases meeting can start late which can cause continuous silence at the beginning (when bots join on time). You can use this parameter to avoid such false positives by adding a buffer before silence detection is activated. ( **Default: 1200(20 minutes)**)

## Using Participant Events   [Skip link to Using Participant Events](https://docs.recall.ai/docs/automatic-leaving-behavior\#using-participant-events)

> ## 📘  Participant Events and Google Meet
>
> Google Meet occasionally emits false positive participant events for meeting bots in calls. Because of this, the participant events heuristic is less reliable in Google Meet calls compared to other platforms.
>
> We recommend using a combination of participant events and [participant names](https://docs.recall.ai/docs/automatic-leaving-behavior#using-participant-names) to produce the most reliable bot detection & automatic leaving behavior across all platforms.

This heuristic relies on marking participants as bots based on their activity in the call. A participant who has not emitted either `active_speaker` or `screenshare_start` for the entire duration of the meeting is marked as a bot.

- `automatic_leave.bot_detection.using_participant_events.timeout`: The number of seconds after which the bot will leave the call if all remaining participants have been marked as bots. ( **Default: 600(10 minutes)**)
- `automatic_leave.bot_detection.using_participant_events.activate_after`: Similar to previous heuristic, this parameter can be used to add a buffer before the heuristic gets activated to avoid false positives. ( **Default: 1200(20 minutes)**)

## Using Participant Names   [Skip link to Using Participant Names](https://docs.recall.ai/docs/automatic-leaving-behavior\#using-participant-names)

This heuristic relies on marking participants as bots based of their name in the meeting.

- `automatic_leave.bot_detection.using_participant_names.matches`: Provide a list of strings which will be substring matched (case insensitively) to every participant name to mark them as a bot. For e.g given `matches: ['notetaker']`, a participant with name `Meeting Notetaker` will be marked as a bot.
- `automatic_leave.bot_detection.using_participant_names.timeout`: The number of seconds after which the bot will leave the call if all remaining participants have been marked as bots
- `automatic_leave.bot_detection.using_participant_names.activate_after`: Similar to previous heuristic, this parameter can be used to add a buffer before the heuristic gets activated to avoid false positives.

_Participant events are generally less reliable than participant names as a heuristic for detecting bots. If your bot names use identifiable phrases such as 'bot', 'notetaker', or your company name, we highly recommend using this for best bot detection accuracy._

Updated 3 months ago

* * *

Did this page help you?

Yes

No

Ask AI