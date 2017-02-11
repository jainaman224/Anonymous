from django_cron import CronJobBase, Schedule

from models import User, Counsellor
from realtime.service import send_sms


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 0  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'realtime.my_cron_job'

    def do(self):
        for each in User.objects.filter(message_sent=False):
            counsellor = Counsellor.objects.get(pk=1)
            if each.sentiment_score > 0.85:
                send_sms(text='Please check the user : ' + each.user_name +
                              ' with phone number : ' +
                              str(each.phone_number), phone_number=counsellor.phone_number)
            elif each.sentiment_score > 0.75:
                send_sms(text='Please consult : ' + counsellor.counsellor_name +
                              ' having phone number : ' +
                              str(counsellor.phone_number), phone_number=each.phone_number)
