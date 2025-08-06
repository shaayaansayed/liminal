---
url: "https://docs.recall.ai/docs/zoom-oauth-faqs"
title: "Zoom OAuth FAQs"
---

## Can we use our existing Zoom OAuth app so users don’t need to OAuth twice?   [Skip link to Can we use our existing Zoom OAuth app so users don’t need to OAuth twice?](https://docs.recall.ai/docs/zoom-oauth-faqs\#can-we-use-our-existing-zoom-oauth-app-so-users-dont-need-to-oauth-twice)

Yes. You can use your existing Zoom OAuth app, as long as it has all required scopes.

If you want to manage the OAuth tokens on your end, instead of having Recall manage the tokens, you can follow the instructions for [Customer Managed OAuth](https://docs.recall.ai/docs/customer-managed-oauth).

## Will we be able to get the join token for local recording with Zoom workspace-level OAuth?   [Skip link to Will we be able to get the join token for local recording with Zoom workspace-level OAuth?](https://docs.recall.ai/docs/zoom-oauth-faqs\#will-we-be-able-to-get-the-join-token-for-local-recording-with-zoom-workspace-level-oauth)

Yes. This integration works for both user-level and workspace-level OAuth.

Zoom Meeting SDK apps only provide user-level OAuth, so you will need to create a separate workspace-level OAuth App. You will also need to submit both your Zoom SDK app and your workspace-level Zoom OAuth App for review.

## Will we be able to get the customer's access token if we use Recall Managed OAuth?   [Skip link to Will we be able to get the customer's access token if we use Recall Managed OAuth?](https://docs.recall.ai/docs/zoom-oauth-faqs\#will-we-be-able-to-get-the-customers-access-token-if-we-use-recall-managed-oauth)

Yes. You can use the [Get Access Token](https://docs.recall.ai/reference/zoom_oauth_credentials_access_token_retrieve) endpoint to fetch the customer's access token, if you're using Recall Managed OAuth. Access tokens generated for Zoom OAuth applications expire after 1 hour.

## What scopes should I request for an Account Level OAuth app?   [Skip link to What scopes should I request for an Account Level OAuth app?](https://docs.recall.ai/docs/zoom-oauth-faqs\#what-scopes-should-i-request-for-an-account-level-oauth-app)

- **user:read:admin**
- **meeting:read:admin**
- **meeting\_token:read:admin:local\_recording**

## My bot uses the Zoom OAuth integration. Why was it still not allowed to record?   [Skip link to My bot uses the Zoom OAuth integration. Why was it still not allowed to record?](https://docs.recall.ai/docs/zoom-oauth-faqs\#my-bot-uses-the-zoom-oauth-integration-why-was-it-still-not-allowed-to-record)

While the Zoom OAuth integration allows bots to record meetings without requesting host permissions every call, the host can still activate a setting that restricts local recording in all of their meetings.

If this setting is active, bots will not be able to record meetings even if OAuth authorization permission has been granted.

This setting can be found in [Zoom settings](https://us06web.zoom.us/profile/setting) under the Recording tab, labelled **“Hosts can give meeting participants permission to record locally."**

## Zoom URL Validation is Failing for my Webhook URL   [Skip link to Zoom URL Validation is Failing for my Webhook URL](https://docs.recall.ai/docs/zoom-oauth-faqs\#zoom-url-validation-is-failing-for-my-webhook-url)

![](https://files.readme.io/79f2b64-CleanShot_2024-05-20_at_12.26.512x.png)

This can happen for a number of reasons. The most common are:

1. The URL you're providing is not correct. Please double check the URL
2. Your Webhook Secret is not configured correctly. Please double check your Webhook Secret is correct.

## Why do I need to provide my `client_id` and `client_secret` if I'm using Customer Managed OAuth?   [Skip link to Why do I need to provide my ](https://docs.recall.ai/docs/zoom-oauth-faqs\#why-do-i-need-to-provide-my-client_id-and-client_secret-if-im-using-customer-managed-oauth)

If you're using Customer Managed OAuth, you don't need to provide the `client_secret` \-\- in the API call you can just provide a dummy string like "a".

We do need the `client_id` however to validate the JWT we receive from your callback URL.

## Why is my published Zoom app failing to join meetings with the `zoom_invalid_signature` error?   [Skip link to Why is my published Zoom app failing to join meetings with the ](https://docs.recall.ai/docs/zoom-oauth-faqs\#why-is-my-published-zoom-app-failing-to-join-meetings-with-the-zoom_invalid_signature-error)

If the Zoom account that owns the your application is removed from your Zoom workspace, your application's SDK keys will stop working as expected. The bot will be unable to join externally-hosted meetings even though your app is published.

You'll need to reach out directly to Zoom support and ask them to transfer ownership of your app to an account that is still within your workspace.

Note: If you do need to remove the account that owns your Zoom app, you should [manually transfer account ownership](https://developers.zoom.us/docs/distribute/app-ownership/transferring-app-ownership/) before removing the account.

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI