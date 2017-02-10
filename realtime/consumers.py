from channels import Group
from channels.sessions import channel_session


def websocket_receive(message):
    text = message.content.get('text')
    print text
    if text:
        Group('chat-1').add(message.reply_channel)
        Group('chat-1').send({"text": text})
        # message.reply_channel.send({"text": "You said: {}".format(text)})
