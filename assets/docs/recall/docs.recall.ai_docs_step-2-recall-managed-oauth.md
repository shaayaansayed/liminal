---
url: "https://docs.recall.ai/docs/step-2-recall-managed-oauth"
title: "Step 2: Recall-Managed OAuth"
---

The last step in the Zoom OAuth integration process is to actually direct your users through the OAuth authorization flow.

Since Recall-managed OAuth manages access and refresh tokens for you, the only two implementation steps necessary are:

1. Directing the user to a Zoom OAuth URL
2. Creating a [Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create) in Recall using the `code` received in the OAuth callback

> ## 📘
>
> For demonstration purposes, we will abstract some of this implementation and pass the authorization code manually through an API request to Recall.
>
> In production, this should be done programmatically in your app, for example by requesting Zoom OAuth permission as part of your onboarding flow, or having your users click a button in your app to connect their Zoom account.

## Registering A Redirect URL   [Skip link to Registering A Redirect URL](https://docs.recall.ai/docs/step-2-recall-managed-oauth\#registering-a-redirect-url)

Under **Basic Information**, add an OAuth Redirect URL (the OAuth Allow List will be automatically updated).

For testing purposes, this can be any URL, though it can be convenient to use a placeholder for a server endpoint that will handle passing this authorization code to Recall for when you implement the end to end user flow. We recommend using a service like Ngrok that can forward requests to your localhost. See this [guide](https://docs.recall.ai/docs/local-webhook-development#ngrok-setup) to get set up with Ngrok.

In the example below, this is set to: `https://my-static-domain.ngrok-free.app/oauth-callback/zoom`

> ## ❗️
>
> Avoid using localhost as a Redirect URL, even for testing. This will throw an error when you get to the final step of creating an OAuth Credential!

![](https://files.readme.io/67446cf-CleanShot_2024-08-01_at_11.57.45.png)

## Constructing a Zoom OAuth URL   [Skip link to Constructing a Zoom OAuth URL](https://docs.recall.ai/docs/step-2-recall-managed-oauth\#constructing-a-zoom-oauth-url)

A Zoom OAuth URL is the URL that you'll be navigating your users to, for them to grant the permissions. For example, you might have a button that says "Connect Zoom", that redirects your user to the OAuth URL.

You can generate the URL using the following code:

TypeScriptPython

```rdmd-code lang-typescript theme-light

function generateAuthUrl(redirectUri: string, zoomAppClientId: string): string {
    const baseUrl = "https://zoom.us/oauth/authorize";
    const queryParams = {
        "response_type": "code",
        "redirect_uri": redirectUri,
        "client_id": zoomAppClientId,
    };
    const queryString = new URLSearchParams(queryParams).toString();
    return `${baseUrl}?${queryString}`;
}

```

```rdmd-code lang-python theme-light

from urllib.parse import urlencode
def generate_auth_url(redirect_uri, client_id):
    base_url = "https://zoom.us/oauth/authorize"
    query_params = {
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "client_id": client_id,
    }
    return base_url + "?" + urlencode(query_params)

```

The `redirect_uri` should exactly match the configured OAuth redirect URL step above.

After calling this function, you should get a URL that looks like the following: [https://zoom.us/oauth/authorize?response\_type=code&redirect\_uri=https%3A%2F%2Fmy-static-domain.ngrok-free.app%2Foauth-callback%2Fzoom&client\_id=YOUR\_CLIENT\_ID\_HERE](https://zoom.us/oauth/authorize?response_type=code&redirect_uri=https%3A%2F%2Fmy-static-domain.ngrok-free.app%2Foauth-callback%2Fzoom&client_id=YOUR_CLIENT_ID_HERE)

Paste this URL into your web browser, and grant the permission when prompted by Zoom.

![](https://files.readme.io/357bdcb-image.png)

## Obtaining the OAuth Code   [Skip link to Obtaining the OAuth Code](https://docs.recall.ai/docs/step-2-recall-managed-oauth\#obtaining-the-oauth-code)

After clicking "Allow", you will be redirected to the `redirect_uri` configured in the previous step.

Since we don't yet have a server running to process this request yet, you will see a page similar to below:

![](https://files.readme.io/5628501-image.png)

This is expected behavior. You now want to look at the URL in your web browser, which should look something like the following: `https://my-static-domain.ngrok-free.app/oauth-callback/zoom?code=JFiSLNVIEejhfiJLmU6AuTnKZQ`

The value in the `code` query parameter is your OAuth code. Save this for the next step.

> ## 🚧  If you're getting "Invalid redirect", check your Redirect URI
>
> The redirect URI specified in the query parameter must match **exactly** the redirect URI registered in the Zoom OAuth App console, **including any trailing slashes**.

## Calling the Recall API   [Skip link to Calling the Recall API](https://docs.recall.ai/docs/step-2-recall-managed-oauth\#calling-the-recall-api)

Now that the user has authorized their account, we can use the OAuth code to register them in the Recall API by calling the [Create Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create) endpoint.

Shell

```rdmd-code lang-shell theme-light

$ curl -X POST https://us-east-1.recall.ai/api/v2/zoom-oauth-credentials/
	-H 'Authorization: ${RECALL_API_KEY}'
 	-H 'Content-Type: application/json'
  -d '{
    "oauth_app": "${RECALL_ZOOM_OAUTH_APP_ID}",
    "authorization_code": {
      "code": "JFiSLNVIEejhfiJLmU6AuTnKZQ",
      "redirect_uri": "${ZOOM_OAUTH_REDIRECT_URI}"
    }
  }'

```

**Example 201 response:**

JSON

```rdmd-code lang-json theme-light

{
  "id":"dadcc9c3-2a6d-4f9a-9467-ff3a2b02a82f",
  "oauth_app":"2d40abfe-c692-4723-b26f-869ebfbde4cf",
  "user_id":"...",                   // Populated for User-managed apps
  "account_id": "...",               // Populated for Admin-managed apps
  "access_token_callback_url": null, // Not applicable, only used for customer-managed OAuth
  "created_at":"2024-04-24T06:38:38.879706Z"
}

```

> ## 🚧  If you're getting "Invalid Grant", check your Redirect URI
>
> The redirect URI sent in this request must match EXACTLY the redirect URI registered in the Zoom OAuth App console, **including any trailing slashes**.

## Handling Re-authorization   [Skip link to Handling Re-authorization](https://docs.recall.ai/docs/step-2-recall-managed-oauth\#handling-re-authorization)

When a user revokes their OAuth permissions, their Zoom OAuth Credential will be marked with a `status` of `unhealthy` in Recall.

If the user tries to re-authorize your app, you should trigger [Create Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create) endpoint with the new authorization code in payload. Recall will update the existing credential instead of creating a new. Depending on the validity of the request the credential's status will also be updated.

Note: This means the `POST` request to [Create Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create) can return existing credential in response(instead of always creating a new credential) and you should adjust your integration to handle this.

Alternatively( **not recommended**), you can choose to delete the `unhealthy` credential and run the authorization flow from scratch for the user. This needs to be done in the exact order as listed below:

1. Remove `unhealthy` credential using [Delete the credential](https://docs.recall.ai/reference/zoom_oauth_credentials_destroy)
2. Prompt the user to re-authenticate your application
3. Create fresh credential using [Create Zoom OAuth Credential](https://docs.recall.ai/reference/zoom_oauth_credentials_create)

Updated about 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI