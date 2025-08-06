---
url: "https://docs.recall.ai/reference/idempotency"
title: "Idempotency"
---

The Recall API supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for all requests with the following methods:

- PUT
- POST
- PATCH

This allows you to retry requests that fail due to networking issues without fear of the the action happening multiple times.

## What are idempotency keys?   [Skip link to What are idempotency keys?](https://docs.recall.ai/reference/idempotency\#what-are-idempotency-keys)

Idempotency keys are a mechanism to prevent accidental duplicate operations by ensuring that repeated requests with the same key are not re-executed.

When our API receives a request containing an idempotency key, it checks whether that key has already been processed. If it has, the server immediately returns the original response from cache instead of running the action again.

## When to use idempotency keys   [Skip link to When to use idempotency keys](https://docs.recall.ai/reference/idempotency\#when-to-use-idempotency-keys)

The primary use cases for idempotency keys include any scenario where a client is unsure whether a previous request actually succeeded. For example:

- There's a transient network failure and you don't receive a response
- A network timeout occurs while creating a resource

By resending the request with the same key, you can be confident that only one resource is created, without knowing whether or not the first action actually succeeded or not.

## Making an idempotent request   [Skip link to Making an idempotent request](https://docs.recall.ai/reference/idempotency\#making-an-idempotent-request)

To make an idempotent request, start by generating a idempotency key.

That key will be used in combination with your user, and the path to identify the request. Pass this key in the `Idempotency-Key` header in your request.

The behavior is as follows:

- If the request is the first request, the endpoint action will be performed as expected
- If another matching request is currently being processed, the endpoint's action will be skipped and you will get a 409
- If another matching request has completed in the previous hour, the endpoint's action will be skipped and you will get the previously completed request's response.

As a best practice, **only generate a new key for each distinct logical operation.**

If you reuse a key for two different actions (even if they involve the same resource configuration), the second request will be treated as a duplicate, and its original result will be returned without performing the action again.

> ## 📘  Idempotency and 507s
>
> If you receive a [507 error](https://docs.recall.ai/reference/errors#adhoc-bot-pool-errors) due to a depleted ad-hoc bot pool, make sure to use a different idempotency key when retrying.
>
> Otherwise, retries will be processed as duplicates of the initial request, and you will continue to receive a 507 response.

Updated about 1 month ago

* * *

Did this page help you?

Yes

No

Updated about 1 month ago

* * *

Did this page help you?

Yes

No