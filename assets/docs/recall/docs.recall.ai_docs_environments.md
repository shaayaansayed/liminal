---
url: "https://docs.recall.ai/docs/environments"
title: "Organization Management"
---

You can manage your organization's users and workspaces in the User Management page of the Recall dashboard.

> ## 📘  View the User Management Dashboard
>
> - [(US) us-east-1](https://us-east-1.recall.ai/dashboard/team)
> - [(Pay-as-you-go) us-west-2](https://us-west-2.recall.ai/dashboard/team)
> - [(EU) eu-central-1](https://eu-central-1.recall.ai/dashboard/team)
> - [(JP) ap-northeast-1](https://ap-northeast-1.recall.ai/dashboard/team)

# Roles   [Skip link to Roles](https://docs.recall.ai/docs/environments\#roles)

Organization-wide roles determine what actions users can perform:

| Role | Description |
| --- | --- |
| Developer | Able to access the dashboard and create API keys. |
| Admin | All the privileges of the "Developer" role. Can also create new workspaces, invite new users, and manage the permissions of other users. |

# User Management   [Skip link to User Management](https://docs.recall.ai/docs/environments\#user-management)

Users can join multiple workspaces in your organization. This allows a single user to have their own development environment while also having access to staging and production environments if desired.

As an admin, you can delegate workspace access for the other users in your workspace.

# Workspaces   [Skip link to Workspaces](https://docs.recall.ai/docs/environments\#workspaces)

You may want to have multiple workspaces to separate different projects, teams, or environments. Each workspace operates independently, with its own settings, users, and API keys.

If you're an Admin in your organization, you can create new workspaces from the Workspace Management page. Users without this role cannot access this page.

# Billing   [Skip link to Billing](https://docs.recall.ai/docs/environments\#billing)

You **do not** have to pay an additional platform fee or other fee in order to use multiple environments.

Any usage will be consolidated under the same billing account as your production credentials.

# FAQs   [Skip link to FAQs](https://docs.recall.ai/docs/environments\#faqs)

## How do I manage dedicated environments?   [Skip link to How do I manage dedicated environments?](https://docs.recall.ai/docs/environments\#how-do-i-manage-dedicated-environments)

You can create a separate workspace per environment in the Recall dashboard. All data is scoped at the workspace level (i.e. bot data, webhook urls, calendars, platform credentials, transcription credentials, etc.) so a separate workspace will ensure the data/configs will be isolated to your environment

Updatedabout 2 months ago

* * *

Did this page help you?

Yes

No

Ask AI