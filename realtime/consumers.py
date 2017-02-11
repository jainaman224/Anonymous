from channels import Group
from channels.sessions import channel_session
from simplejson import dumps

from realtime.models import Session, User, Message
from realtime.service import update_user_sentiment


def ws_connect(message):
    room_id = message['path'].strip('/').split('/')[0]
    message.reply_channel.send({"accept": True})
    Group('chat-%s' % room_id).add(message.reply_channel)


def websocket_receive(message):
    room_id = message['path'].strip('/').split('/')[0]
    user_id = message['path'].strip('/').split('/')[1]
    text = message.content.get('text')
    Group('chat-%s' % room_id).send({'text': text})
    update_user_sentiment.after_response(user_id=user_id, text=text)


def ws_disconnect(message):
    room_id = message['path'].strip('/').split('/')[0]
    Group("chat-%s" % room_id).discard(message.reply_channel)
