import subprocess

from django_cron import CronJobBase, Schedule

'''
def executeCommand(st, debug = False):
    cmd_data = subprocess.Popen(st, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output,error = cmd_data.communicate()
    x = output[18:-20].replace("\"","").replace(" ","").split(",")
    return int(x[0][6:9]), int(x[2][6:9])

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'

    def do(self):
        msg = Message.objects.all()
        for each in msg:
            if msg.is_processed == False:
                a = 'text='
                b = 'msg.message'
                x, y = executeCommand(['curl', '-d', a+b, 'http://text-processing.com/api/sentiment/'])
                #User.objects.get(id=msg.user).
'''