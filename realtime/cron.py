from django_cron import CronJobBase, Schedule

from models import User

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'realtime.my_cron_job'

    def do(self):
        for each in User.objects.all():
            if each.sentiment_score > 0.85:
                # TODO: trigger psycharistic to consult user and message to police
                pass
            elif each.sentiment_score > 0.75:
                # TODO: trigger suggest to user to consult psycharistic and message to ngo
                pass
