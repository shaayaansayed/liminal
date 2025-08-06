---
url: "https://docs.recall.ai/docs/zoom-sdk-review-guidelines"
title: "Technical Questions & Details"
---

As part of submitting your Zoom SDK App, you must answer some questions regarding your app's technology, security, and privacy.

You must also provide a test plan for the app reviewer to follow in order to successfully test your application.

# Technical Design & Privacy Attestation   [Skip link to Technical Design & Privacy Attestation](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#technical-design--privacy-attestation)

* * *

## Application Overview   [Skip link to Application Overview](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#application-overview)

![](https://files.readme.io/1ab819a-image.png)

### Technology Stack   [Skip link to Technology Stack](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#technology-stack)

The majority of your response to this question should be dependent on the rest of your application.

You can include the sentence "We use the Recall.ai meeting bot service to capture audio and video data from meetings." to describe your usage of Recall.ai

### Architecture Diagram   [Skip link to Architecture Diagram](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#architecture-diagram)

You should provide an architecture diagram showing Recall.ai as an external API. [Here](https://drive.google.com/file/d/1W83D05CmU4efiHAicI-MjdFr_zK23ykI/view) is the architecture diagram of the Recall.ai service to attach to your diagram as an appendix if necessary.

### Application Development   [Skip link to Application Development](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#application-development)

These questions are not related to the Recall.ai service.

> ## 📘
>
> Don't worry if you answer "No" to questions 1-3 in the Application Development section - Zoom will not reject your app based on these answers.

* * *

## Security Overview   [Skip link to Security Overview](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#security-overview)

![](https://files.readme.io/10f6ab9-image.png)

### Question 1   [Skip link to Question 1](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-1)

Recall.ai's service meets these standards. You should answer "Yes" if the other parts of your service meet this standard, and "No" if they do not.

### Question 2:   [Skip link to Question 2:](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-2)

Answer "Yes" if you are using the Recall Zoom OAuth integration. If you are handling the webhooks yourself, answer "Yes" or "No" depending on your specific implementation.

### Question 3:   [Skip link to Question 3:](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-3)

Answer "Yes" if you are using the Recall Zoom OAuth integration. If you are handling this integration yourself, answer "Yes" or "No" depending on your specific implementation.

If you are using the Recall Zoom OAuth integration, you can answer as follows: "My application uses Recall.ai to capture data from the Zoom meeting. Metadata captured by Recall.ai, including Zoom OAuth tokens, is encrypted at rest using AWS RDS database encryption. Media such as audio and video is encrypted at rest using AWS S3 bucket encryption. Recall.ai retains the data for only 7 days before permanently deleting it."

Also include details on how your application handles user data after it's ingested into your systems.

* * *

## Privacy Attestations   [Skip link to Privacy Attestations](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#privacy-attestations)

![](https://files.readme.io/fc67141-image.png)

### Question 1:   [Skip link to Question 1:](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-1-1)

Recall.ai does not require recording or chat scopes, so you may answer with the following:

"We do not use any Recording or Chat scopes in our application."

### Question 2 - 7, 9-10   [Skip link to Question 2 - 7, 9-10](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-2---7-9-10)

Recall.ai's service does not do any of these things. Answer "Yes" or "No" depending on the other parts of your app.

### Question 8   [Skip link to Question 8](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-8)

Recall.ai's is considered a "fourth party". You should check "Yes". A text box will appear, asking for more detail. A example answer would be the following:

"We disclose data to Recall.ai, which is a meeting bot API we use to capture data from meetings. Our contract with Recall.ai limits their use, maintenance, and disclose of such data to the language in our privacy statement."

![](https://files.readme.io/f84dcbb-image.png)

### Question 11   [Skip link to Question 11](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-11)

The Recall.ai service does not mandate any retention, as you can delete any captured data immediately using the [Delete Bot Media](https://docs.recall.ai/reference/bot_delete_media_create) endpoint. Answer depending on the retention the rest of your application requires.

### Question 12 - 15   [Skip link to Question 12 - 15](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#question-12---15)

Your usage of the Recall.ai service does not affect any of these answers.

# Scopes   [Skip link to Scopes](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#scopes)

* * *

## Required Scopes   [Skip link to Required Scopes](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#required-scopes)

By default, you don't need to request **any** scopes, since the SDK credentials are only used for the bot to authenticate itself.

If you want to use the [Recall Zoom OAuth Integration](https://docs.recall.ai/reference/zoom-oauth-integration), and you don't have an existing OAuth app already in the marketplace, you can request the [scopes outlined here](https://docs.recall.ai/reference/zoom-oauth-integration#1-requesting-the-required-scopes)

If you are not using the Recall Zoom OAuth Integration, **do not** request any additional scopes as they will be unused. Zoom will not approve your app during review if you have unused scopes, and this is the #1 cause of app denials we see during the review process.

Now that your Zoom credentials are configured in the Recall dashboard, you can send a bot to a Zoom meeting by calling the `Create Bot` endpoint.

## Scope Usage Description   [Skip link to Scope Usage Description](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#scope-usage-description)

Several OAuth scopes are required for the Recall Zoom OAuth integration. The following are guidelines for writing the scope usage description required during the app review process.

## /meeting:read   [Skip link to /meeting:read](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#meetingread)

- The meeting:read scope is used to list a user's meetings, in order to determine which upcoming meetings are owned by the user we have OAuthed on to. This is necessary, as we must know who the creator of the meeting is to retrieve the local recording token.

### /user:read (Only required for Account Level Apps)   [Skip link to /user:read (Only required for Account Level Apps)](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#userread-only-required-for-account-level-apps)

- The user:read scope is used to list the users in an account. This is necessary, as we need to list all upcoming meetings created by all users in the account, and this scope will be used to get a list of users.

### /meeting\_token:read:local\_recording   [Skip link to /meeting_token:read:local_recording](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#meeting_tokenreadlocal_recording)

- The meeting\_token:read:local\_recording scope is used to generate a local recording token. This token will be used by our Zoom SDK based meeting bot to automatically begin recording once it joins the call.

### /user\_zak:read (Automatically populated on Zoom SDK apps)   [Skip link to /user_zak:read (Automatically populated on Zoom SDK apps)](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#user_zakread-automatically-populated-on-zoom-sdk-apps)

- This scope is unused, however cannot be removed from a Zoom SDK app.

# Zoom SDK OAuth Compliance Review Document   [Skip link to Zoom SDK OAuth Compliance Review Document](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#zoom-sdk-oauth-compliance-review-document)

You will receive a document over Google Docs titled "Zoom SDK OAuth Compliance Review", asking questions about how the Zoom SDK is being used. Because this is all handled by Recall, the following are our recommended responses: [https://docs.google.com/document/d/1ZAf9vEt3AqxaO7n2kM3tJQGI1599YSNvd14xFA3vAsU/edit?usp=sharing](https://docs.google.com/document/d/1ZAf9vEt3AqxaO7n2kM3tJQGI1599YSNvd14xFA3vAsU/edit?usp=sharing)

# Test Plan   [Skip link to Test Plan](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#test-plan)

* * *

In order for your app to be approved, the Zoom app reviewer needs to test that the meeting bot is functioning as expected. To do this, you should provide a test plan in your submission with a set of test credentials the reviewer can use.

Zoom is looking to verify a few things when conducting the test:

1. All requested scopes are actually being used.
2. The bot that joins the call is using the correct set of SDK credentials.
3. The bot that joins the call is requesting recording permission in line with Zoom's new requirements.

We recommend putting together the test plan with a Loom/video walkthrough. It can sometimes be difficult to explain what your app is doing in text, in a way that the Zoom app reviewer will understand. Including a short video tutorial can avoid unnecessary back-and-forth due to misunderstandings.

We have 2 recommended test plan outlines, depending on if you're using the [Recall Zoom OAuth Integration](https://docs.recall.ai/reference/zoom-oauth-getting-started).

## Test Plan Outline - Not using Recall Zoom OAuth Integration   [Skip link to Test Plan Outline - Not using Recall Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#test-plan-outline---not-using-recall-zoom-oauth-integration)

1. Instructions on how to log in to the application using the test credentials provided.
2. Instructions on how to send the bot to a call.
1. Point out that the bot sends a recording permission request dialog to the host, and only starts recording once it's been granted permission by the host.
2. Point out that the bot displays the recording consent notification once it starts recording.
3. Point out that the [active apps notifier](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063928) shows that your SDK app is currently active in the call.

## Test Plan Outline - Using Recall Zoom OAuth Integration   [Skip link to Test Plan Outline - Using Recall Zoom OAuth Integration](https://docs.recall.ai/docs/zoom-sdk-review-guidelines\#test-plan-outline---using-recall-zoom-oauth-integration)

1. Instructions on how to log in to the application using the test credentials provided.
2. Instructions on how to connect your Zoom account via OAuth.
1. Explain that the requested credentials are used to keep track of which meetings belong to the user, so that a "Join token for local recording" can be retrieved from the Zoom API when a bot is sent to the call.
3. Instructions on how to send the bot to a call.
1. Point out that the bot automatically has recording permission because the bot was able to get a "Join token for local recording" using the scopes requested earlier.
2. Point out that the bot displays the recording consent notification once it starts recording.
3. Point out that the [active apps notifier](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063928) shows that your SDK app is currently active in the call.

> ## 📘  Note about unapproved app credentials
>
> While unapproved Zoom SDK Credentials won't work for users outside of your Zoom workspace, they will work for your Zoom app reviewer without any additional configuration.

Updated 7 months ago

* * *

Did this page help you?

Yes

No

Ask AI