---
url: "https://docs.recall.ai/docs/step-2-alternative-customer-managed-oauth"
title: "Step 2 Alternative: Customer-Managed OAuth"
---

> ## ℹ️
>
> In general, we recommend using [Recall-Managed OAuth](https://docs.recall.ai/docs/recall-managed-oauth) unless:
>
> - You already have an integration with the Zoom OAuth API.
> - You need to call the Zoom API endpoints for other functionality in your app.

When using the Recall Zoom OAuth integration, you also have the option to manage the access and refresh tokens for users on your end.

In this case, you provide Recall a callback URL where our integration can retrieve OAuth access tokens for your users.

## Setting Up a Callback URL   [Skip link to Setting Up a Callback URL](https://docs.recall.ai/docs/step-2-alternative-customer-managed-oauth\#setting-up-a-callback-url)

You will need to expose a callback URL on your server which responds to an HTTP GET request with the OAuth access token for the user you're connecting. Your endpoint should:

1. Validate the request is coming from Recall. It is insecure to expose an unauthenticated endpoint that returns user access tokens!
2. Fetch the access\_token for the correct user. **Note: Recall requires access tokens to be valid for at least 120 seconds into the future. Access tokens that are too close to expiry will be rejected.**
3. Return the access token as a plain-text HTTP response body.

The recommended approach to achieve requirements #1 and #2 is to encode a credential and/or a user-id in the URL. For example, your URL scheme could be `https://your-website.example/api/callbacks?user-id=0001&auth_token=supersecrettoken`, and your HTTP request handler could validate the `auth_token` query parameter, and return the access\_token for user `0001`.

Here's a sample implementation in pseudocode:

Pseudocode

```rdmd-code lang-Text theme-light

def verify_request_is_from_recall(request):
	...

def get_user_id_from_request(request):
  ...

def get_access_token_by_user_id(user_id):
  ...

def handle_request(request):
  if not verify_request_is_from_recall(request):
    return "Error"

  user_id = get_user_id_from_request(request)
  access_token = get_access_token_by_user_id(user_id)
  return get_access_token

```

## Registering the Callback URL in the Recall API   [Skip link to Registering the Callback URL in the Recall API](https://docs.recall.ai/docs/step-2-alternative-customer-managed-oauth\#registering-the-callback-url-in-the-recall-api)

You'll want to call the [Create Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create) endpoint, providing the publicly accessible callback URL. This endpoint will make a request to the provided endpoint, and validate that the token returned is valid and meets the requirements.

When the token is returned, Recall builds a mapping between the user and this callback URL. This is how we know when to call this particular URL when we need an access token for a specific user.

When we call this endpoint, your server must return a response within 5 seconds or the request will time out and fail.

**Note: Every user on your end should have their own Zoom OAuth Credential registered with Recall. This means that each user should have a unique callback URL.**

Shell

```rdmd-code lang-text theme-light

$ curl -X POST https://us-east-1.recall.ai/api/v2/zoom-oauth-credentials/
	-H 'Authorization: Token YOUR-RECALL-API-KEY'
 	-H 'Content-Type: application/json'
  -d '{
    "oauth_app": "YOUR-RECALL-ZOOM-OAUTH-APP-ID",
    "access_token_callback_url": "YOUR-URL-HERE",
  }'


{
  "id":"dadcc9c3-2a6d-4f9a-9467-ff3a2b02a82f",
  "oauth_app":"YOUR-RECALL-OAUTH-APP-ID",
  "user_id":"redacted",
  "account_id":null,
  "access_token_callback_url":"YOUR-URL-HERE",
  "created_at":"2023-08-03T06:38:38.879706Z"
}

```

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI