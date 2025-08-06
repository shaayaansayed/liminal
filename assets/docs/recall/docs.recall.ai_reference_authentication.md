---
url: "https://docs.recall.ai/reference/authentication"
title: "Authentication"
---

# API Keys   [Skip link to API Keys](https://docs.recall.ai/reference/authentication\#api-keys)

API keys are used to authenticate to the Recall.ai platform.

You can create and manage your API keys in the Recall dashboard:

- [(US) us-east-1](https://us-east-1.recall.ai/dashboard/api-keys)
- [(Pay-as-you-go) us-west-2](https://us-west-2.recall.ai/dashboard/api-keys)
- [(EU) eu-central-1](https://eu-central-1.recall.ai/dashboard/api-keys)
- [(JP) ap-northeast-1](https://ap-northeast-1.recall.ai/dashboard/api-keys)

> ## 📘
>
> API keys belong to individual users, but access is environment-scoped. This means that multiple accounts under the same environment share access to the same resources, but have their own API keys.

# HTTP Header: Token Authorization   [Skip link to HTTP Header: Token Authorization](https://docs.recall.ai/reference/authentication\#http-header-token-authorization)

All requests must be authenticated via token in the HTTP `Authorization` header in the following format:

```rdmd-code lang- theme-light
Authorization: Token YOUR_API_KEY

```

For e.g if you Recall API Key is `abcdefghijklmnopqrst` then the following should be the authorization header

```rdmd-code lang- theme-light
Authorization: Token abcdefghijklmnopqrst

```

Unauthenticated requests will receive a 401 error: `401: Unauthorized`.

Updated 3 months ago

* * *

Did this page help you?

Yes

No

Updated 3 months ago

* * *

Did this page help you?

Yes

No