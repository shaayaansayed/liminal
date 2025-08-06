---
url: "https://docs.recall.ai/docs/sub-codes"
title: "Bot Sub Codes"
---

Sub codes are a field ( `sub_code`) added to certain [bot status change](https://docs.recall.ai/reference/bot-status-change-events) events to provide extra context.

Here's an example of a status change object structure:

JSON

```rdmd-code lang-json theme-light

{
  "code": "call_ended",
  "sub_code": "bot_kicked_from_call",
  "updated_at": "2023-04-28T08:51:37.741790Z"
}

```

Here, we can interpret this status change as follows:

- **Code:** `call_ended` \- The status change event category (Call Ended)
- **Sub Code:** `bot_kicked_from_call` \- The underlying reason for the status change (sub code)

# Sub Code Types   [Skip link to Sub Code Types](https://docs.recall.ai/docs/sub-codes\#sub-code-types)

Currently there are 3 distinct sub code categories:

- [Call Ended Sub Codes](https://docs.recall.ai/docs/sub-codes#call-ended-sub-codes)
- [Fatal Sub Codes](https://docs.recall.ai/docs/sub-codes#fatal-sub-codes)
- [Recording Permission Denied (Zoom only)](https://docs.recall.ai/docs/sub-codes#recording-permission-denied-sub-codes)

| Sub Code Type | Event | Platforms |
| --- | --- | --- |
| Call Ended | `call_ended` | All |
| Fatal | `fatal` | All |
| Recording Permission Denied | `recording_permission_denied` | Zoom |

Note: Platform specific `sub_code` is prefixed with platform name (e.g `zoom_sdk_credentials_missing`)

> ## 🚧  We may add additional sub\_codes
>
> You should not treat the `sub_code` as an enum, as we may add values in the future without prior notice. We will never remove values without notifying all our customers and a long depreciation period, as we consider removing values a breaking change.

## Recording Permission Denied Sub Codes   [Skip link to Recording Permission Denied Sub Codes](https://docs.recall.ai/docs/sub-codes\#recording-permission-denied-sub-codes)

Since Zoom bots have a few extra requirements to meet for recording, there are more places that bots can run into trouble.

When a bot fails to record in a Zoom call, the `recording_permission_denied` webhook event will include a Zoom-specific sub code that provides more context into the reason it failed.

These `sub_code` will be added to the `recording_permission_denied` event.

| Sub Code | Description |
| --- | --- |
| `zoom_local_recording_disabled` | The meeting host has their global user-level local recording setting disabled. [More info](https://docs.recall.ai/docs/common-zoom-recording-errors#the-hosts-local-recording-setting-is-disabled)<br>The host was _not_ presented with the recording consent popup. |
| `zoom_local_recording_request_disabled` | The meeting host has their user-level local recording setting enabled, but the has disabled the advanced recording option labelled "Hosts can give meeting participants permission to record locally". [More info](https://docs.recall.ai/docs/common-zoom-recording-errors)<br>The host was _not_ presented with the recording consent popup. |
| `zoom_local_recording_request_disabled_by_host` | The meeting host has disabled participants from requesting local recording permission or has denied all future requests. [More info](https://docs.recall.ai/docs/common-zoom-recording-errors#the-host-has-disabled-requesting-recording-permission-within-the-current-call)<br>The host was _not_ presented with the recording consent popup. |
| `zoom_bot_in_waiting_room` | The bot is in the waiting room due to which local recording cannot be requested.<br>The host was _not_ presented with the recording consent popup. |
| `zoom_host_not_present` | The host was not present in the meeting when the bot requested local recording permission.<br>This only occurs in very rare cases where the bot ​does​ request permission when the host isn't present. One example is when a host leaves/disconnects right as the bot requests permissions. |
| `zoom_local_recording_request_denied_by_host` | The host denied the bot's local recording request.<br>The host _was_ presented with the recording consent popup. |
| `zoom_local_recording_denied` | The request to record was denied by the user.<br>This indicates that the user has local recording disabled in their global user settings, the recording request popup was presented and denied, or that the popup was presented but the request time out. |
| `zoom_local_recording_grant_not_supported` | The meeting host is using Zoom Room or other Zoom client that does not support local recording permission. |
| `zoom_sdk_key_blocked_by_host_admin` | The Zoom SDK key used by the bot is blocked by the Zoom user's workspace admin. |

## Call Ended Sub Codes   [Skip link to Call Ended Sub Codes](https://docs.recall.ai/docs/sub-codes\#call-ended-sub-codes)

The `call_ended` event signifies that a bot left, or was removed from, the call.

Recall attaches a `sub_code` to these events to expose the underlying reason why the bot is no longer in the call. This can be for obvious reasons such as the host ending the call ( `call_ended_by_host`), but sometimes its less obvious why a bot left a call.

Below is a list of all call ended sub codes and what they mean.

| Sub Code | Description |
| --- | --- |
| `call_ended_by_host` | The call has been ended by the meeting host. |
| `call_ended_by_platform_idle` | The call has been ended by the meeting platform, because it was idle. |
| `call_ended_by_platform_max_length` | The call has been ended by the meeting platform because it reached the maximum meeting length. For instance, on Zoom, the maximum length of a meeting when on a free account is [40 minutes](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067966). |
| `call_ended_by_platform_waiting_room_timeout` | The bot could not join the call because meeting platform's maximum waiting room time exceeded.<br>For Google Meet, this is 10 minutes. Zoom and Teams don't have a timeout. |
| `timeout_exceeded_waiting_room` | The bot left the call because it was in the waiting room for too long.<br>This is the timeout specified by [`automatic_leave.waiting_room_timeout`](https://docs.recall.ai/docs/automatic-leaving-behavior). |
| `timeout_exceeded_noone_joined` | The bot left the call because nobody joined the call for too long. |
| `timeout_exceeded_everyone_left` | The bot left the call because everyone else left. |
| `timeout_exceeded_silence_detected` | The bot left the call because all other participants were likely bots based off continuous silence detection heuristic. |
| `timeout_exceeded_only_bots_detected_using_participant_names` | The bot left the call because all other participants were likely bots based off participant names heuristic. |
| `timeout_exceeded_only_bots_detected_using_participant_events` | The bot left the call because all other participants were likely bots based off participant events heuristic. |
| `timeout_exceeded_in_call_not_recording` | The bot left the call because it never started recording e.g. remained in the `in_call_not_recording` state for longer than [`automatic_leave.in_call_not_recording_timeout`](https://docs.recall.ai/reference/bot_create) |
| `timeout_exceeded_in_call_recording` | The bot left the call because it exceeded the timeout set in [`automatic_leave.in_call_recording_timeout`](https://docs.recall.ai/reference/bot_create) . |
| `timeout_exceeded_recording_permission_denied` | The bot left the call because it exceed the timeout set in [recording\_permission\_denied\_timeout](https://docs.recall.ai/reference/bot_create) |
| `timeout_exceeded_max_duration` | _Pay-as-you-go only:_ The bot exceeded its maximum duration. |
| `bot_kicked_from_call` | The bot was removed from the call by the host. |
| `bot_kicked_from_waiting_room` | The bot was removed from the waiting room by the host. |
| `bot_received_leave_call` | The bot received leave call request. |

## Fatal Sub Codes   [Skip link to Fatal Sub Codes](https://docs.recall.ai/docs/sub-codes\#fatal-sub-codes)

When a bot hits a fatal error, a `fatal` event is emitted with an attached `sub_code` that provides more context. Below is a list of possible fatal sub codes, their meaning, and any recommended action to take, if any.

| sub\_code | Message | Recommended action |
| --- | --- | --- |
| `bot_errored` | The bot ran into an unexpected error. |  |
| `meeting_not_found` | No meeting was found at the given link. |  |
| `meeting_not_started` | The meeting has not started yet. |  |
| `meeting_requires_registration` | The meeting requires registration. | Currently not supported for MS Teams.<br>For Zoom, see [Registration-Required Meetings & Webinars](https://docs.recall.ai/docs/registration-required-meetings-webinars). |
| `meeting_requires_sign_in` | The meeting can only be joined by signed in users. | Incase of Zoom bots, this error message means that the Zoom meeting has [only authenticated users can join](https://support.zoom.us/hc/en-us/articles/360060549492-Allowing-only-authenticated-users-in-meetings) enabled. By default, the bot is unauthenticated, so it cannot join these calls.<br>To bypass this error, follow the steps in [Joining "Sign In Required" Zoom Meetings](https://docs.recall.ai/reference/joining-sign-in-required-zoom-meetings).<br>For MS Teams, see [Signed-In Microsoft Teams Bots](https://docs.recall.ai/docs/microsoft-teams-bot-login).<br>For Google Meet, see [Signed-In Google Meet Bots](https://docs.recall.ai/docs/google-meet-login-getting-started). |
| `meeting_link_expired` | The meeting link has expired. |  |
| `meeting_link_invalid` | The meeting does not exist or the link is invalid. |  |
| `meeting_password_incorrect` | The meeting password is incorrect. |  |
| `meeting_locked` | The meeting is locked. |  |
| `meeting_full` | The meeting is full. |  |
| `meeting_ended` | The bot attempted to join a meeting that has already ended and can no longer be joined. |  |
| `google_meet_internal_error` | The bot errored due to a Google Meet internal issue. |  |
| `google_meet_sign_in_failed` | The bot was not able to sign in to google. |  |
| `google_meet_sign_in_captcha_failed` | The bot was not able to sign in to google because of captcha. |  |
| `google_meet_bot_blocked` | The bot was disallowed from joining the meeting. | Review [Google Meet: FAQ](https://docs.recall.ai/docs/google-meet-faq#why-did-my-bot-fail-to-join-a-meeting-with-google_meet_bot_blocked-status-code) for common causes. |
| `google_meet_sso_sign_in_failed` | The bot was not able to sign in to google with SSO. |  |
| `google_meet_sign_in_missing_login_credentials` | The bot was not able to sign in to google because login credentials were not configured. | Create an [Authenticated Google Meet Bot](https://docs.recall.ai/docs/google-meet-login-getting-started) to allow your bots to join sign-in-only Google Meet meetings. |
| `google_meet_sign_in_missing_recovery_credentials` | The bot was not able to sign in to google because recovery credentials were not configured. |  |
| `google_meet_sso_sign_in_missing_login_credentials` | The bot was not able to sign in to google with SSO because login credentials were not configured. |  |
| `google_meet_sso_sign_in_missing_totp_secret` | The bot was not able to sign in in to google with SSO because TOTP secret was missing from password. |  |
| `google_meet_video_error` | The bot was not able to join the call due to Google Meet video error. |  |
| `google_meet_meeting_room_not_ready` | The bot was not able to join the call as the meeting room was not ready. |  |
| `google_meet_login_not_available` | There were not enough available logins (Google accounts) in the supplied `google_login_group_id` for the bot to use. | Create additional Google logins as outlined [here](https://recallai.readme.io/docs/google-meet-login-getting-started#5-adding-more-logins). |
| `google_meet_permission_denied_breakout` | The bot tried to join an active Google Meet breakout room and was rejected. | N/A |
| `zoom_sdk_credentials_missing` | The bot was not able to join because Zoom SDK credentials were not configured. |  |
| `zoom_sdk_update_required` | A newer version of the Zoom SDK is required to join this meeting. |  |
| `zoom_sdk_app_not_published` | The SDK credentials configured in Recall dashboard have not been approved by Zoom. Bots using unapproved Zoom credentials can only join meetings hosted in the workspace of the user that created the credentials. | In order for your bot to join calls outside of your Zoom workspace, you must submit your Zoom app for approval. |
| `zoom_email_blocked_by_admin` | The Zoom account this bot is joining from has been disallowed to join this meeting by the Zoom workspace administrator. |  |
| `zoom_registration_required` | The bot failed to join because registration is required for this Zoom meeting. |  |
| `zoom_captcha_required` | The bot failed to join because captcha is required for this Zoom meeting. |  |
| `zoom_account_blocked` | The account this bot is joining from has been blocked by Zoom. | When providing the bot with a [ZAK token](https://docs.recall.ai/docs/zoom-signed-in-bots), generate the ZAK token from a different Zoom user account. |
| `zoom_invalid_join_token` | Zoom's SDK rejected the join token provided by the bot. This can happen due to an expired token, the token missing permissions (for instance, being generated for the wrong meeting), or the token being invalid. |  |
| `zoom_invalid_signature` | The Zoom SDK was not able to generate a valid meeting-join signature.<br>This could mean that your Zoom SDK credentials are invalid, or the meeting link is malformed. | Follow [this guide](https://recallai.readme.io/docs/set-up-zoom#create-zoom-api-credentials) to set up Zoom credentials.<br>Double check that your meeting link is correct. |
| `zoom_internal_error` | The bot errored due to an internal Zoom error. |  |
| `zoom_join_timeout` | The request to join the Zoom meeting timed out. |  |
| `zoom_email_required` | The bot failed to join because providing an email is required to join this Zoom meeting. | Provide a `zoom.user_email` when creating the bot as outlined in [Email Required Meetings](https://docs.recall.ai/docs/zoom-email-required-meetings). |
| `zoom_web_disallowed` | The Zoom meeting host has disallowed joining from the web which prevents the bot from joining the meeting. | Have the host disable E2E encryption for the meeting.<br>If E2E encryption support is required by the user, you can use the Zoom Native bot to join these meetings. |
| `zoom_connection_failed` | The bot failed to join the meeting due to a Zoom server error. |  |
| `zoom_error_multiple_device_join` | The bot failed to join the meeting due to another participant with the same credentials having joined the meeting. |  |
| `zoom_meeting_not_accessible` | The Zoom meeting was not accessible for the bot. |  |
| `zoom_meeting_host_inactive` | The request to join the Zoom meeting failed, as the meeting host has been disabled or restricted. You will not be able to join this meeting. |  |
| `zoom_invalid_webinar_invite` | The invite to the Zoom webinar was invalid. Check the password and any tokens passed in. |  |
| `microsoft_teams_call_dropped` | The bot got call dropped error from MS Teams and was unable to re-join the call. |  |
| `microsoft_teams_sign_in_credentials_missing` | The bot failed to join a Microsoft Teams meeting requiring all participants to be signed-in. The bot was not signed in and thus was not able to join the call. |  |
| `microsoft_teams_sign_in_failed` | The bot failed to join a Microsoft Teams meeting requiring all participants to be signed-in. The bot was not signed in or failed to sign in to its configured Microsoft account. | If Teams credentials are not set up, follow the [Signed-In Teams Bot Setup](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams) guide. |
| `microsoft_teams_internal_error` | The bot errored due to a Microsoft Teams server error. |  |
| `microsoft_teams_captcha_detected` | The bot failed to join due to captcha being enabled for anonymous participants. | Use [Signed-In Microsoft Teams Bots](https://docs.recall.ai/docs/microsoft-teams-bot-login) to bypass this. The tenant must also have the domain of the account used to sign-in whitelisted as a [trusted organization](https://learn.microsoft.com/en-us/microsoftteams/trusted-organizations-external-meetings-chat?tabs=organization-settings#specify-trusted-microsoft-365-organizations) if required by their security settings. |
| `microsoft_teams_bot_not_invited` | The bot failed to join a Microsoft Teams meeting as it was not the account that was invited. | Follow this [Sign in with a different account to join this meeting](https://learn.microsoft.com/en-us/microsoftteams/troubleshoot/meetings/external-participants-join-meeting-blocked#error-2-sign-in-with-a-different-account-to-join-this-meeting) guide to allow access to the bot. |
| `microsoft_teams_breakout_room_unsupported` | The bot was moved to a Microsoft Teams breakout room, but they are not supported by Recall. |  |
| `microsoft_teams_event_not_started_for_external` | The bot failed to join a Microsoft Teams meeting that prevents external participants from joining before the event begins. |  |
| microsoft\_teams\_2fa\_required |  | Your signed-in Teams bot has 2FA configured. Disable this by [following this guide](https://docs.recall.ai/docs/setting-up-signed-in-bots-for-microsoft-teams#step-21-disabling-security-defaults) to resolve the error. |
| `webex_join_meeting_error` | The bot failed to join a Webex meeting because the meeting was invalid, or Webex credentials are not set up properly. | If Webex credentials are not set up, follow the [Webex Bot Setup](https://docs.recall.ai/docs/webex-bot-setup) guide. |

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI