import os

from slack_bolt import App, Say

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# {'token': '6NsjTdTM06B4fXpO2Jl8DbjF', 'team_id': 'T9JSCTEQ6', 'api_app_id': 'A026P7K6ZHV',
# 'event': {
#   'type': 'reaction_added', 'user': 'U9K5JG4LX',
#   'item': {'type': 'message', 'channel': 'CVDTDDQPP', 'ts': '1625583629.003600'},
#   'reaction': 'doge3d', 'item_user': 'U9K5JG4LX', 'event_ts': '1625583843.004200'
#  },
# 'type': 'event_callback',
# 'event_id': 'Ev027KTHU36V', 'event_time': 1625583843,
# 'authorizations': [{
# 'enterprise_id': None, 'team_id': 'T9JSCTEQ6',
# 'user_id': 'U026XAABRBQ', 'is_bot': True, 'is_enterprise_install': False
# }],
# 'is_ext_shared_channel': False, 'event_context': '2-reaction_added-T9JSCTEQ6-A026P7K6ZHV-CVDTDDQPP'}

# {'ok': True,
# 'user': {
# 'id': 'U9K5JG4LX', 'team_id': 'T9JSCTEQ6', 'name': 'weber0593',
# 'deleted': False, 'color': 'e7392d', 'real_name': 'Chris Weber',
# 'tz': 'America/New_York', 'tz_label': 'Eastern Daylight Time', 'tz_offset': -14400,
# 'profile': {'title': '', 'phone': '', 'skype': '', 'real_name': 'Chris Weber', 'real_name_normalized': 'Chris Weber',
# 'display_name': 'Chris', 'display_name_normalized': 'Chris', 'fields': None, 'status_text': '', 'status_emoji': '',
# 'status_expiration': 0, 'avatar_hash': '9a1d74805d46', 'image_original':
# 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_original.png',
# 'is_custom_image': True,
# 'image_24': 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_24.png',
# 'image_32': 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_32.png',
# 'image_48': 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_48.png', 'image_72':
# 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_72.png', 'image_192':
# 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_192.png',
# 'image_512': 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_512.png',
# 'image_1024': 'https://avatars.slack-edge.com/2021-05-21/2099268172916_9a1d74805d467ff3568a_1024.png',
# 'status_text_canonical': '', 'team': 'T9JSCTEQ6'},
# 'is_admin': True, 'is_owner': True, 'is_primary_owner': False, 'is_restricted': False,
# 'is_ultra_restricted': False, 'is_bot': False, 'is_app_user': False, 'updated': 1625255952,
# 'is_email_confirmed': True}}

@app.event("reaction_added")
def handle_reaction_added_events(body, event, logger, say: Say):
    print("Hello world I got a reaction!")
    user_id = event["user"]
    reaction = event["reaction"]
    user = app.client.users_info(user=user_id)
    username = user["user"]["profile"]["display_name"]
    print(username)

    result = app.client.conversations_history(
        channel=event["item"]["channel"],
        inclusive=True,
        oldest=event["item"]["ts"],
        limit=1
    )
    message = result["messages"][0]
    print(message["text"])
    say(text=f"Thanks for the {reaction} reaction {username}!", thread_ts=event["item"]["ts"])
    say(text=f"You reacted to the message: {message['text']}", thread_ts=event["item"]["ts"])


@app.event("app_mention")
def handle_app_mention_events(body, logger):
    print("This is a mention event!")
    logger.info(body)


if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 8000)))