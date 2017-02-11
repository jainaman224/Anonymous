import os
import subprocess

import plivo

from realtime.models import User


def execute_command(command):
    cmd_data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cmd_data.communicate()
    x = output[18:-20].replace("\"", "").replace(" ", "").split(",")
    return float(int(x[0][6:10])) / 10000


def update_user_sentiment(user_id, text):
    user = User.objects.get(pk=user_id)
    data = 'text=' + text
    negative_value = execute_command(['curl', '-d', data, 'http://text-processing.com/api/sentiment/'])
    user.sentiment_score = (3 * user.sentiment_score + negative_value) / 4
    user.save()


def send_sms(text, phone_number):
    p = plivo.RestAPI(os.environ['pilvo_auth_id'], os.environ['constant.pilvo_auth_token'])
    params = {
        'src': 'VK-FINMOI',
        'dst': '+91' + str(phone_number),
        'text': text
    }
    p.send_message(params)
