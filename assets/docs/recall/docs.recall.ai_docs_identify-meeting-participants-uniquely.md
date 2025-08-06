---
url: "https://docs.recall.ai/docs/identify-meeting-participants-uniquely"
title: "Identify Meeting Participants Uniquely"
---

Depending on your use case, you might want to be able to identify participants across meetings.

Meeting platforms don't expose the email addresses of participants, though there are some some ways to achieve identify participants uniquely across meetings.

## Calendar integration   [Skip link to Calendar integration](https://docs.recall.ai/docs/identify-meeting-participants-uniquely\#calendar-integration)

If you're using the calendar integration, you can map users to emails of calendar invites to get their emails.

- Fuzzy match on calendar event participants
- Use email address as ID

Benefit: Works across meeting platforms

Con: doesn't work 100% of the time

## Zoom: `user_conf_id`   [Skip link to Zoom: ](https://docs.recall.ai/docs/identify-meeting-participants-uniquely\#zoom-user_conf_id)

The `conf_user_id` is a unique identifier for a Zoom account that can be relied upon to be consistent across meetings. The `user_guid` field is not consistent across meetings, and should not be relied upon to track Zoom accounts.

```rdmd-code lang- theme-light
{
  "id": 16998240,
  "name": "John Smith",
  "is_host": true,
  "platform": "desktop",
  "extra_data": {
    "zoom": {
      "os": 2,
      "guest": false,
      "user_guid": "EF3AL77C-49AB-6F8A-A947-61C6AB57D6E6",
			"conf_user_id": "RiajKBaChMxzJAmuF90nln"
    }
  }
}

```

## Teams `user_id`   [Skip link to Teams ](https://docs.recall.ai/docs/identify-meeting-participants-uniquely\#teams-user_id)

The `user_id` is a unique identifier for a Teams account that can be relied upon to be consistent across meetings.

```rdmd-code lang- theme-light
{
  "role": "organizer",
  "meeting_role": "organizer",
  "participant_type": "inTenant",
  "user_id": "8:orgid:780027c1-2d8e-4783-849f-8eeaf1f08525",
  "tenant_id": "c21986f7-3b64-42ba-82f8-df1c6b90ec77",
  "client_version": "CallSignalingAgent (...)"
}

```

The `meeting_role` can be `organizer`, `attendee`, or `presenter`. For more information on each of these roles, see [Microsoft's documentation](https://support.microsoft.com/en-us/office/roles-in-microsoft-teams-meetings-c16fa7d0-1666-4dde-8686-0a0bfe16e019).

For information about Teams `participant_type`'s, please see [User Types in Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/apps-in-teams-meetings/teams-apps-in-meetings#user-types-in-teams).

Updated 6 days ago

* * *

Did this page help you?

Yes

No

Ask AI