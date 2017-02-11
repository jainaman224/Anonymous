import subprocess
from realtime.models import User


def execute_command(command):
    cmd_data = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cmd_data.communicate()
    x = output[18:-20].replace("\"", "").replace(" ", "").split(",")
    return float(int(x[0][6:10]))/10000


def update_user_sentiment(user_id, text):
    user = User.objects.get(pk=user_id)
    data = 'text=' + text
    negative_value = execute_command(['curl', '-d', data, 'http://text-processing.com/api/sentiment/'])
    user.sentiment_score = (3*user.sentiment_score + negative_value) / 4
    user.save()