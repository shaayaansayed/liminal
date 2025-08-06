---
url: "https://docs.recall.ai/docs/common-zoom-recording-errors"
title: "Common Zoom Recording Errors"
---

# Host was not present   [Skip link to Host was not present](https://docs.recall.ai/docs/common-zoom-recording-errors\#host-was-not-present)

Sometimes a bot joins a meeting but is unable to record because it never asked for permission. In this case, this means the host was not present and thus was unable to grant recording permissions to the bot.

You'll be able to identify this scenario because the bot's `status_changes` will neither have a `recording_permission_allowed` or `recording_permission_denied` event and will remain in the `in_call_not_recording` state until it times out or the call is ended.

In order for a bot to get recording permissions when the host is not present in the meeting, the creator of the meeting must be authenticated via the [Zoom OAuth Integration](https://recallai.readme.io/reference/zoom-oauth-getting-started).

> ## 📘  But the user said they were the host and were present, why are they showing as `is_host: false`?
>
> If the end user that created the meeting is not showing up as the host, one of two things is going on:
>
> - They are not signed into the Zoom account where the meeting was created from
> - They are not signed into their Zoom client at all

# The host's local recording setting is disabled   [Skip link to The host's local recording setting is disabled](https://docs.recall.ai/docs/common-zoom-recording-errors\#the-hosts-local-recording-setting-is-disabled)

If the host's global local recording setting is disabled, the bot will fail to record.

In this case, the bot will have a Recording Permission Denied event with a `zoom_local_recording_disabled` [Sub Code](https://docs.recall.ai/docs/sub-codes).

**How to fix:** Host should enable their global user-level local recording setting in their Zoom user settings:

![](https://files.readme.io/5bc34923062608d743f856336ecb583004ca6d0e375d87d84c3d8be82111b58f-CleanShot_2024-12-13_at_13.45.492x.png)

# The host has disabled permitting participants to record locally   [Skip link to The host has disabled permitting participants to record locally](https://docs.recall.ai/docs/common-zoom-recording-errors\#the-host-has-disabled-permitting-participants-to-record-locally)

In this case, the host has their **global** local recording setting enabled, but they can't grant participants permission to record locally, which is needed for a bot to record.

The bot will emit a Recording Permission Denied event with a `zoom_local_recording_request_disabled` [Sub Code](https://docs.recall.ai/docs/sub-codes).

**How to fix:** Host should enable this setting by checking the boxes labelled:

- Internal meeting participants
- External meeting participants

![](https://files.readme.io/64d9e339178e3ef395de054795ca787b27c2e241ead9115b475cbbb58f40bdb3-CleanShot_2024-09-27_at_16.48.14.png)

# The host has disabled requesting recording permission within the current call   [Skip link to The host has disabled requesting recording permission within the current call](https://docs.recall.ai/docs/common-zoom-recording-errors\#the-host-has-disabled-requesting-recording-permission-within-the-current-call)

If the host has the proper user-level recording settings set up properly on the Zoom website, but has disabled the option to allow participants to request local recording _within the call_, the bot will not be able to record.

In this case, the bot will emit a Recording Permission Denied event with a `zoom_local_recording_request_disabled_by_host` [Sub Code](https://docs.recall.ai/docs/sub-codes).

**How to fix:** Host should enable this setting within the call:

![](https://files.readme.io/b4a00d5-zoom_local_recording_request_disabled_by_host.png)

# Zoom internal error   [Skip link to Zoom internal error](https://docs.recall.ai/docs/common-zoom-recording-errors\#zoom-internal-error)

On rare occasions, your bot may fail to enter a call with a `zoom_internal_error` [sub code](https://docs.recall.ai/docs/sub-codes).

Unfortunately this means something went wrong on Zoom's end, and we have limited visibility into the underlying error. We do our best to handle these errors internally through retries but on rare occasions this error can cause a bot to fail.

If you're seeing this error recur for a certain situation or user, please let us know and we can raise the issue with Zoom.

# Host never received the recording consent popup   [Skip link to Host never received the recording consent popup](https://docs.recall.ai/docs/common-zoom-recording-errors\#host-never-received-the-recording-consent-popup)

In certain cases, a user may report that the bot never recorded and they never received a recording consent popup to grant recording permissions.

When this happens:

- The bot will have neither a `recording_permission_allowed` nor a `recording_permission_denied` event
- None of the `meeting_participants` on the bot will have `is_host` as `true`

This is the same situation as the [host not being present](https://docs.recall.ai/docs/common-zoom-recording-errors#host-was-not-present), but in this case, the end user that created the meeting was actually in the call.

If the host claimed they were present, but no participant is shown as the host, it's likely that the user joined the Zoom call while signed into a different Zoom user than the one that the meeting was created from.

Many users have multiple Zoom accounts and they'll need to ensure they're joining the meetings from the same account as the one they're creating meetings from. If the end user needs to support granting recording permissions from various Zoom accounts, they can assign their alternative account(s) as [alternative hosts](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067027).

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI