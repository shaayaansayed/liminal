---
url: "https://docs.recall.ai/docs/zoom-new-bot-requirements"
title: "Zoom Announces New Bot Requirements"
---

On July 17th 2023, Zoom announced a set of updates to formalize the concept of meeting bots. Most importantly, they have added bot compliance requirements that **must** be followed for the bots to continue functioning.

# Where was this announced?   [Skip link to Where was this announced?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#where-was-this-announced)

An email was sent announcing these changes, but only to developers that have created their own Zoom Meeting SDK keys. If you haven't created your own Meeting SDK keys in the past, you would not have gotten this email from Zoom. Here is the email for reference:

![Image 1: Zoom announcement](https://files.readme.io/b0708fd-Screenshot_2023-07-30_at_3.33.34_PM.png)

Image 1: Zoom announcement

_Relevant linked resources in this email_

- [https://developers.zoom.us/docs/distribute/sdk-app-requirements/](https://developers.zoom.us/docs/distribute/sdk-app-requirements/)
- [https://developers.zoom.us/docs/zoom-apps/guides/meeting-bots-sdk-media-streams/](https://developers.zoom.us/docs/zoom-apps/guides/meeting-bots-sdk-media-streams/)

# What are the Zoom compliance changes?   [Skip link to What are the Zoom compliance changes?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#what-are-the-zoom-compliance-changes)

Zoom is enforcing:

1. All bots must be created with the Zoom Meeting SDK.
2. All bots must get recording permission, and display the standard Zoom recording disclaimer.
3. All Zoom SDK keys must go through the review process.

## Recording Permission + Zoom Recording Disclaimer   [Skip link to Recording Permission + Zoom Recording Disclaimer](https://docs.recall.ai/docs/zoom-new-bot-requirements\#recording-permission--zoom-recording-disclaimer)

All bots must show the Zoom standard recording disclaimer when they begin recording. The recording disclaimer consists of 3 elements:

1. A pop up to all users that says "This meeting is being recorded"
2. An audio announcement that says "This meeting is being recorded"
3. The "🔴 Recording" symbol in the top left corner of Zoom while the meeting is being recorded

This is all built into Zoom, and elements can't be edited or omitted.

![Image 1: Recording disclaimer screenshot](https://files.readme.io/3446293-Screenshot_2023-07-30_at_4.38.07_PM.png)

Image 2: Recording disclaimer screenshot

> ## 📘  The only way to trigger this recording disclaimer is for the bot to get permission from the host to record the meeting.

There are 2 ways to get this recording permission from the host.

### Method 1: Have the host grant the bot recording permission manually   [Skip link to Method 1: Have the host grant the bot recording permission manually](https://docs.recall.ai/docs/zoom-new-bot-requirements\#method-1-have-the-host-grant-the-bot-recording-permission-manually)

- When the bot joins the meeting, it will pop up a notification that is only visible to the host (Image 3)
- This pop up will appear for the host for every single meeting, regardless of if you check the box that says "Apply these permissions to all future requests".
- If the host clicks "Deny", you will receive a webhook from Recall that the request to record has been denied.
- If the host clicks "Allow Recording", the bot will receive recording permission and begin recording. This will trigger the recording disclaimer. (Image 2)
- This pop up is not dismissable until the host chooses an option.

![Image 2: Bot recording request screenshot](https://files.readme.io/a73e478-Screenshot_2023-07-30_at_4.37.41_PM.png)

Image 3: Bot recording request screenshot

> ## ℹ️  Method 1 is the default behavior. No code change is required on your end.

### Method 2: Have the host authorize their Zoom account   [Skip link to Method 2: Have the host authorize their Zoom account](https://docs.recall.ai/docs/zoom-new-bot-requirements\#method-2-have-the-host-authorize-their-zoom-account)

Recall provides a [Zoom OAuth Integration](https://docs.recall.ai/reference/zoom-oauth-getting-started) that allows bots to automatically record the call without triggering a pop-up, if the meeting host has authorized their account.

This authorization is a one-time setup process, and [we recommend](https://docs.recall.ai/reference/product-best-practices) making this authorization part of your onboarding flow.

The authorization can either be at the Zoom user level, or at the Zoom workspace level. Workspace-level authorization means that all meetings created in that workspace can be automatically recorded.

> ## 👍  We highly recommend Method 2. There will be some code changes required.

## Zoom SDK Key Review Process   [Skip link to Zoom SDK Key Review Process](https://docs.recall.ai/docs/zoom-new-bot-requirements\#zoom-sdk-key-review-process)

The Zoom bot is built on top of the Zoom Meeting SDK. All customers will need to create their own Zoom SDK key and submit it to be reviewed by Zoom.

We recommend creating a **new** Zoom SDK key [here](https://marketplace.zoom.us/develop/create) and submit it for review. We recommend against submitting an existing Zoom SDK key if you have one.

Once the SDK key is approved by Zoom, you can put it into the Recall dashboard [here](https://api.recall.ai/dashboard/platforms/zoom).

> ## ❗️  Do not input your Zoom SDK Credentials into your production Recall account dashboard before Zoom has approved them.
>
> Bots using unapproved Zoom SDK Credentials will **only** be able to join meetings created in the SDK developer's workspace. Therefore, if these credentials are rolled out on your production account before approval, the bot will be unable to join any of your customers' meetings.

# How can I become compliant?   [Skip link to How can I become compliant?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#how-can-i-become-compliant)

- For the Zoom recording disclaimer, Recall will take care of triggering the Zoom Recording Disclaimer pop up.
- If you want to allow your users to record automatically, Recall provides a [Zoom OAuth Integration](https://docs.recall.ai/reference/zoom-oauth-getting-started) to enable automatic recording **without host intervention.**
- You should create a **new** Zoom SDK key [here](https://marketplace.zoom.us/develop/create) and submit it for review.

# When is the deadline to become compliant?   [Skip link to When is the deadline to become compliant?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#when-is-the-deadline-to-become-compliant)

> ## ❗️  The first wave of enforcement is October 16th 2023.

Zoom is enforcing compliance on a cohort basis. The deadline for the first cohort is October 16th.

- If you don't have your own Zoom SDK keys, you **are** in the first cohort.
- If you have your own Zoom SDK keys, you will have received an email from Zoom if you are in the first cohort.

**If you are unsure, please check with us!** We highly recommend completing the compliance process before October 16th even if you aren't part of the first cohort, as the Zoom SDK key review process can take 2-3 weeks.

# What are next steps?   [Skip link to What are next steps?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#what-are-next-steps)

1. Follow the [Zoom OAuth Integration Guide](https://docs.recall.ai/reference/zoom-oauth-getting-started) to setup the Recall+Zoom OAuth integration.
2. Submit your [Zoom SDK Key for review](https://docs.recall.ai/reference/zoom-sdk-review-guidelines).
3. Review our [Zoom Bot Product Best-Practices](https://docs.recall.ai/reference/product-best-practices) and make any necessary product changes.

# FAQ   [Skip link to FAQ](https://docs.recall.ai/docs/zoom-new-bot-requirements\#faq)

### 1\. Can we customize the recording disclaimer?   [Skip link to 1. Can we customize the recording disclaimer?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#1-can-we-customize-the-recording-disclaimer)

Unfortunately, the recording disclaimer cannot be customized. The audio announcement, words and buttons in the pop up, and recording symbol in the top left corner all are part of the Zoom permissioning framework and cannot be changed.

### 2\. If only transcription is being accessed, do we still need to show the recording disclaimer?   [Skip link to 2. If only transcription is being accessed, do we still need to show the recording disclaimer?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#2-if-only-transcription-is-being-accessed-do-we-still-need-to-show-the-recording-disclaimer)

Yes. We have verified with our contacts at Zoom -- if any meeting data is being accessed you will need to show this disclaimer.

### 3\. Why doesn't the August 17th deadline that is specified in the email apply?   [Skip link to 3. Why doesn't the August 17th deadline that is specified in the email apply?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#3-why-doesnt-the-august-17th-deadline-that-is-specified-in-the-email-apply)

The August deadline in the email (Image 1) only affects Zoom SDK apps that your users must install. It doesn't affect the bot because the bot does not require installation from the user. We have confirmed this with our multiple contacts at Zoom.

### 4\. When we go through the Zoom SDK Key publishing process, does this mean our app will be listed on the Zoom Marketplace?   [Skip link to 4. When we go through the Zoom SDK Key publishing process, does this mean our app will be listed on the Zoom Marketplace?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#4-when-we-go-through-the-zoom-sdk-key-publishing-process-does-this-mean-our-app-will-be-listed-on-the-zoom-marketplace)

Yes. Your Zoom SDK app will be listed on the Zoom Marketplace. If you don't want the SDK app to be publicly listed, you can mention in the Zoom publishing review notes that you don't want your app to be listed.

### 5\. How long does the Zoom SDK Key review take?   [Skip link to 5. How long does the Zoom SDK Key review take?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#5-how-long-does-the-zoom-sdk-key-review-take)

It typically takes 2-3 weeks.

### 6\. Is a pentest required for the zoom app review   [Skip link to 6. Is a pentest required for the zoom app review](https://docs.recall.ai/docs/zoom-new-bot-requirements\#6-is-a-pentest-required-for-the-zoom-app-review)

No, it is not required. However, in Zoom's words, if you don’t have a third party pentest:

> It would be helpful to provide the Zoom review team with additional documents that demonstrate that you developed your application with security in mind.
>
> This can be in the form of an SSDLC, security/privacy policy for your users, an incident response plan, dependency management policy etc. For an SSDLC, it is typically a written document (can be as short as a page, as long as it’s comprehensive) that outlines the security design of your app from requirements, through development, to production.

We will be providing sample documentation as part of our technical migration guide we'll be releasing in the next few weeks.

### 7\. Apply these settings to future meetings - what does this checkbox actually do?   [Skip link to 7. Apply these settings to future meetings - what does this checkbox actually do?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#7-apply-these-settings-to-future-meetings---what-does-this-checkbox-actually-do)

This checkbox currently has incorrect wording. It's actual effect is that for **the duration of the current meeting**, if another participant/bot requests permission later on, the response that is selected (Approve/Deny) will be applied to that request as well. It does not apply to future meetings.

### 8\. Bot consent flow doesn’t work for hosts that use the web client. When will this be fixed?   [Skip link to 8. Bot consent flow doesn’t work for hosts that use the web client. When will this be fixed?](https://docs.recall.ai/docs/zoom-new-bot-requirements\#8-bot-consent-flow-doesnt-work-for-hosts-that-use-the-web-client-when-will-this-be-fixed)

We have checked with our contacts at Zoom and although it is on their radar, there doesn't seem to be a concrete timeline to fix this.

Updatedover 1 year ago

* * *

Did this page help you?

Yes

No

Ask AI