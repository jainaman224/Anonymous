import subprocess

import after_response

from realtime.models import User


def execute_command(command):
    cmd_data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cmd_data.communicate()
    x = output[18:-20].replace("\"", "").replace(" ", "").split(",")
    return int(x[0][6:9]), int(x[2][6:9])


@after_response.enable
def update_user_sentiment(user_id, text):
    user = User.objects.get(pk=user_id)
    data = 'text=' + text
    negative_value, positive_value = execute_command(['curl', '-d', data, 'http://text-processing.com/api/sentiment/'])
    user.sentiment_score = str(positive_value)
    user.save()
