---
url: "https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging"
title: "Testing Your Zoom OAuth Integration"
---

Once you've gone through the [Zoom OAuth Setup](https://docs.recall.ai/docs/integration-guide-zoom-oauth) and either [Recall-Managed](https://docs.recall.ai/docs/recall-managed-oauth) or [Customer Managed OAuth](https://docs.recall.ai/docs/customer-managed-oauth), you should test your integration.

This guide walks you through the questions to answer to ensure your integration is working properly.

## Can Users Complete the OAuth Flow Successfully?   [Skip link to Can Users Complete the OAuth Flow Successfully?](https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging\#can-users-complete-the-oauth-flow-successfully)

Use your own Zoom account or a test account and ensure it can go through the OAuth flow as expected.

After going through the flow, call the [List Zoom OAuth Credentials](https://docs.recall.ai/reference/zoom_oauth_credentials_list) endpoint and ensure your credentials are being created in Recall properly.

## Are Zoom Meetings Synchronized Properly?   [Skip link to Are Zoom Meetings Synchronized Properly?](https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging\#are-zoom-meetings-synchronized-properly)

You can make a request to the List Zoom Meeting to OAuth Credential Mappings endpoint to see the list of meetings the Recall integration has synced, along with the OAuth credentials that were used to sync the meetings.

To test if your meetings are being created properly in Recall for your OAuth'ed Zoom account:

- Create a new meeting
- Call [List Zoom Meeting to OAuth Credential Mappings](https://docs.recall.ai/reference/zoom_meetings_to_credentials_list)
- Ensure the meeting exists in the response

Any meetings in this list will be automatically recorded by bots sent to them.

Shell

```rdmd-code lang-Text theme-light

curl -X GET <https://us-east-1.recall.ai/api/v2/zoom-meetings-to-credentials>
	-H 'Authorization: Token YOUR-RECALL-API-KEY'

// Response
{
  "next": null,
  "previous": null,
  "results": [\
    {\
      "meeting_id": 12347589873,\
      "credential": "dadcc9c3-2a6d-4f9a-9467-ff3a2b02a82f",\
      "synced_at": "2023-08-03T06:38:39.011715Z"\
    },\
    {\
      "meeting_id": 84731728293,\
      "credential": "dadcc9c3-2a6d-4f9a-9467-ff3a2b02a82f",\
      "synced_at": "2023-08-03T06:38:39.009752Z"\
    }\
  ]
}

```

## Can a Bot Record Zoom Meetings Automatically?   [Skip link to Can a Bot Record Zoom Meetings Automatically?](https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging\#can-a-bot-record-zoom-meetings-automatically)

Since you've confirmed your Zoom account is registered with the Recall Zoom OAuth integration, and that all your upcoming meetings are be automatically synced, any bots sent to these meetings should be able to record automatically.

1. Create an instant Zoom meeting (make sure the account is the same as the one you OAuth'ed)
2. Sending a bot to the meeting by calling [Create Bot](https://docs.recall.ai/reference/bot_create)
3. Make sure the bot joins the meeting, and records properly with no popup.

# Bot Logs   [Skip link to Bot Logs](https://docs.recall.ai/docs/zoom-oauth-sync-status-and-debugging\#bot-logs)

* * *

There are a few [Bot Logs](https://docs.recall.ai/docs/debugging-bots#bot-logs) related to Zoom specifically:

- `zoom_join_token_fetch_using_zoom_oauth_failed`
- `zoom_third_party_recording_token_fetch_using_zoom_oauth_failed`

| Error Code | Explanation |
| --- | --- |
| `zoom_join_token_fetch_using_zoom_oauth_failed` | The bot attempted to fetch a join token for local recording using the Zoom OAuth Integration OAuth and failed.<br>If you **are** using the [Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-oauth-integration) , this could indicate the meeting host has not installed your OAuth app, or something else went wrong.<br>If you are **not** using the Zoom OAuth integration, this can be safely ignored.<br>The bot will fall-back to prompting the host for recording permission manually. |
| `zoom_third_party_recording_token_fetch_using_zoom_oauth_failed` | This indicates that the bot attempted to fetch a [Zoom 3rd Party Recording Token](https://docs.recall.ai/docs/zoom-3rd-party-recording-token) using OAuth and failed.<br>This could indicate the 3rd Party Recording Token feature is not enabled on the meeting host's Zoom account, but may also indicate that the credentials have become invalidated.<br>If you are **not** using the 3rd party recording token, this can be safely ignored.<br>The bot will fall-back to prompting the host for recording permission manually. |

Updated 6 months ago

* * *

- [Zoom OAuth FAQs](https://docs.recall.ai/docs/zoom-oauth-faqs)

Did this page help you?

Yes

No

Ask AI