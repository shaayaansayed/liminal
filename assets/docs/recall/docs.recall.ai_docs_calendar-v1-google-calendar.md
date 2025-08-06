---
url: "https://docs.recall.ai/docs/calendar-v1-google-calendar"
title: "Google Calendar"
---

Recall allows your users to sync their google calendar and set auto recording preferences for their meetings.

### Creating Google OAuth 2.0 Client   [Skip link to Creating Google OAuth 2.0 Client](https://docs.recall.ai/docs/calendar-v1-google-calendar\#creating-google-oauth-20-client)

To enable this feature, first setup an OAuth2.0 client following the steps below.

1. Obtain Google OAuth 2.0 client credentials. You can follow the steps provided here [https://support.google.com/googleapi/answer/6158849?hl=en](https://support.google.com/googleapi/answer/6158849?hl=en).

2. Enable **Google Calendar API** in the project. More info here [https://support.google.com/googleapi/answer/6158841](https://support.google.com/googleapi/answer/6158841)

3. Configure permission scopes `calendar.events.readonly` & `userinfo.email` in the consent screen section.


![](https://files.readme.io/0d351f1-Screenshot_2023-05-24_at_10.11.44_AM.png)

4. Add `https://us-east-1.recall.ai/api/v1/calendar/google_oauth_callback/` as a redirect URI for the OAuth client id. (\_Note: For development purpose, see [below](https://docs.recall.ai/docs/calendar-v1-google-calendar#submitting-google-oauth-client-to-production) for moving app to production/submitting for verification\_)

![](https://files.readme.io/ee046a5-Screenshot_2022-06-02_at_9.10.15_AM.png)

5. Save the client credentials in your Recall workspace. [https://us-east-1.recall.ai/dashboard/platforms/google](https://us-east-1.recall.ai/dashboard/platforms/google)

![](https://files.readme.io/2935fc7-Screenshot_2022-06-02_at_9.09.02_AM.png)

### Building Google OAuth 2.0 URL   [Skip link to Building Google OAuth 2.0 URL](https://docs.recall.ai/docs/calendar-v1-google-calendar\#building-google-oauth-20-url)

Each user in your application must connect their Google calendar via OAuth before using calendar integration. The process for connection is triggered by redirecting user to the OAuth URL.

The URL structure should be as follows:

```rdmd-code lang- theme-light
https://accounts.google.com/o/oauth2/v2/auth?
    scope={SCOPES}
    &access_type=offline
    &prompt=consent
    &include_granted_scopes=true
    &response_type=code
    &state={STATE}
    &redirect_uri={REDIRECT_URI}
    &client_id={CLIENT_ID}

```

1. SCOPES


This parameter should be space seperated string containing required scopes which are `calendar.events.readonly` & `userinfo.email`.

Sample value:

```rdmd-code lang- theme-light
https://www.googleapis.com/auth/calendar.events.readonly https://www.googleapis.com/auth/userinfo.email

```

2. REDIRECT\_URI


This parameter should be one of the `redirect_uri` s configured in your Google OAuth 2.0 client.

3. CLIENT\_ID


This parameter should be your Google OAuth 2.0 client's `client_id` property.

4. STATE


This parameter needs to be a JSON stringified object, which should contain


a. `recall_calendar_auth_token`: The calendar auth token for the user. ( **required**)


b. `google_oauth_redirect_url`: The redirect\_uri (should be same as REDIRECT\_URI parameter in the url) ( **required**)


c. `success_url`: The URL to redirect the user to once authentication has completed (optional)


d. `error_url`: The URL to redirect the user if the authentication errored (optional)


Sample value:

```rdmd-code lang- theme-light
state=JSON.stringify({
  recall_calendar_auth_token: AUTH_TOKEN_HERE,
  google_oauth_redirect_url: REDIRECT_URI_HERE,
  success_url: https://yourdomain.com/google-calendar-connection/success,
  error_url: https://yourdomain.com/google-calendar-connection/success,
})

```

# Going to Production: Getting Approval   [Skip link to Going to Production: Getting Approval](https://docs.recall.ai/docs/calendar-v1-google-calendar\#going-to-production-getting-approval)

The first step in the approval process is to fill out your app information. You should do so at the following link: [https://console.cloud.google.com/apis/credentials/consent/edit](https://console.cloud.google.com/apis/credentials/consent/edit)

![657](https://files.readme.io/1ff5761-2022-11-01_20-44.png)

The next step is to select the scopes you are requesting through the OAuth interaction. The 2 scopes you require for the Recall Calendar integration are

1. **`calendar.events.readonly` (sensitive scope)**
2. **`userinfo.email` (non-sensitive scope)**

For the "How will the scopes be used?" section, you should explain why your app requires calendar permissions as well as any other scopes you request. In terms of the calendar permissions specifically, something like:

"We need access to the /auth/calendar.events.readonly scope in order to automatically record our user's video conference meetings on their "primary" calendar. We read event data in order to find video conference events that our users have scheduled."

The demo video should walk through the process of signing up to your app, approving the permissions through the OAuth flow, and showing the interface to sync and mark meetings to be recorded. [This is the official guide](https://support.google.com/cloud/answer/9110914?authuser=2#verification-requirements&zippy=%2Cwhat-are-the-requirements-for-verification) to the elements that need to be shown in the app demonstration video.

![](https://files.readme.io/8a0e521-Screenshot_2023-07-11_at_11.40.04_AM.png)

> ## 🚧  Remember to update your Redirect URI before submitting!
>
> If your redirect URI is `recall.ai` or any other domain that you don't own, Google **will** reject your submission.

Before submitting your Google OAuth Application to production, please ensure to update the `redirect_uri` to be on your own domain (rather than being on recall.ai domain) as Google requires to verify domain ownership of each of the redirect URIs added in the app.

For example, add `https://your_website_domain/api/google_oauth_callback` as `redirect_uri`. In the request handler for above URL, return a HTTP redirect response to /a `https://us-east-1.recall.ai/api/v1/calendar/google_oauth_callback/`.

**All request query parameters should be forwarded as is from your domain to recall.ai's OAuth endpoint.**

Updated 11 months ago

* * *

Did this page help you?

Yes

No

Ask AI