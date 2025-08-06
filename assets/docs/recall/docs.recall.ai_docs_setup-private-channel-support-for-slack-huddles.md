---
url: "https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles"
title: "Setup Private Channel Support for Slack Huddles"
---

# Setup   [Skip link to Setup](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#setup)

## Step 1: Create a Slack team integration with Recall   [Skip link to Step 1: Create a Slack team integration with Recall](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#step-1-create-a-slack-team-integration-with-recall)

Use this [guide](https://docs.recall.ai/docs/slack-huddle-bots-integration-guide#step-1-configure-your-webhook-in-your-app) to create and setup a Slack team integration with Recall if you do not have an active integration already setup.

## Step 2: Create your Slack application   [Skip link to Step 2: Create your Slack application](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#step-2-create-your-slack-application)

1. Navigate to [https://api.slack.com/apps?new\_app=1](https://api.slack.com/apps?new_app=1) and select “From scratch”
2. Enter your Slack application’s name. This should reflect your brand as it will be visible to all end-users.
3. Select a workspace to develop it in. This will just be for testing–you’ll be able to add it to all your end-users’ workspaces.
4. Click “Create App”

## Step 3: Update Slack application permissions   [Skip link to Step 3: Update Slack application permissions](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#step-3-update-slack-application-permissions)

1. Navigate to “OAuth & Permissions”
2. In “Redirect URLs”, add your product’s redirect URL to process the Slack authorization grant
3. Click "Save URLs"
4. Under “User Token Scopes” in “Scopes”, click “Add an OAuth Scope” and add the following: `channels:read`, `groups:read`, `im:read`, `mpim:read`, `team:read` and `users:read`

> ## 🚧  You may need to go through Slack app review if listed on Slack Marketplace
>
> If your Slack app is already listed on the Slack Marketplace, adding new scopes requires an app review. This process can take up to 8 weeks and typically involves regular communication with Slack’s review team. Please note that Slack’s approval process is thorough and has strict requirements, so approval isn’t guaranteed even with provided justifications. However, if your app already uses some or all of the required scopes listed above, **no further action** or additional justifications are needed, provided your existing setup meets Slack’s standards.
>
> If your app already has these scopes, you’re good to go and can fully utilize our integration. If not, you can still benefit from partial integration functionality as long as you have at least one relevant permission. For example, having `channels:read` will enable the integration to detect huddles in private channels.
>
> If your app is _not_ listed on the Slack Marketplace, you are not required to go through app review and can still distribute your app.

> ## 📘  Note about changing scopes in distributed Slack applications
>
> Modifying Slack application scopes requires your end-users to re-authorize your application to grant updated permissions. This process may not be simple for all use cases, so we encourage you to think about what is most appropriate for your product's user base. You may choose to only work with private channels for existing end-users, but grant extended functionality to private group and direct message channels for new users who authorize your Slack application.

## Step 4: Onboard Users   [Skip link to Step 4: Onboard Users](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#step-4-onboard-users)

1. In your Slack application's dashboard, navigate to "Manage Distribution"
2. Under "Share Your App with Other Workspaces", expand all collapsible sections and follow the steps to prepare your application for public unlisted distribution
3. Click "Activate Public Distribution"
4. Navigate to "Basic Information" and take note of the following values: Client ID and Client Secret
5. Navigate to "OAuth & Permissions" and take note of all the scopes listed
6. Programmatically generate your [OAuth URL](https://api.slack.com/authentication/oauth-v2#how) to allow users to authorize your application into their workspace, separating your scopes with a `:` character and properly URL escaping them


```rdmd-code lang- theme-light
https://slack.com/oauth/v2/authorize?scope={{YOUR APPLICATION BOT SCOPES}}&user_scope={{YOUR APPLICATION USER SCOPES}}&redirect_uri={{YOUR REDIRECT URI}}&client_id={{YOUR CLIENT ID}}&state={{CRYPTOGRAPHICALLY SECURE RANDOM IDENTIFIER}}

```

7. Give this URL to your end-users, such as through a button in your product

> ## 📘  Ensure `state` is unique and securely verifiable
>
> As is with all OAuth integrations, the `state` query parameter must be unique and securely verifiable by your product. Common approaches include using CSPRNG-generated values or JSON Web Tokens. Upon redirect to your product after the end-user authorizes your Slack application, you must be able to verify the authenticity of the `state` value and ensure it cannot be replayed. Failing to do so opens your product up to security vulnerabilities.

## Step 5: Forward user credentials to Recall   [Skip link to Step 5: Forward user credentials to Recall](https://docs.recall.ai/docs/setup-private-channel-support-for-slack-huddles\#step-5-forward-user-credentials-to-recall)

1. On redirect to your app, get the authorization code and call our user [OAuth token API](https://docs.recall.ai/reference/slack_teams_oauth_tokens_create)

Python

```rdmd-code lang-python theme-light

def slack_oauth_redirect_page(request):
  query_params = request.query
  state = query_params["state"]
  if not verify_state_securely(state):
		return StatusCode(401)
  authorization_code = query_params["code"]
  oauth_data = {
    "code": code,
    "client_id": "{{YOUR CLIENT ID}}",
    "client_secret": "{{YOUR CLIENT SECRET}}",
  }
  response = requests.post(
       "https://slack.com/api/oauth.v2.access", data=oauth_data
  )
  response_data = response.json()
	if not response_data.get("ok"):
    return StatusCode(400)
  access_token = authed_user.get("access_token")
	send_code_to_recall_oauth_token_api(access_token)

```

After adding your user’s OAuth token, we’ll automatically start detecting applicable channels and monitoring for new private huddles in them periodically (may take up to several minutes).

> ## 📘
>
> Your integration can only monitor private huddles in channels where **at least one member has authorized the app**. This means it may not knock on every private huddle across the workspace. It will only knock on the private channels where it has visibility via an authorized user.
>
> Adoption is still beneficial because **the more users who install the app, the more private channels it can cover**. Full workspace adoption isn’t required for private channel support.

Updated 10 days ago

* * *

Did this page help you?

Yes

No

Ask AI