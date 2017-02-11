import hashlib
import os

import datetime
from django.db import models

from django_cron import CronJobBase, Schedule

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #red_buffer = models.FloatField(default=0.0)
    forum_room_id = models.IntegerField()
    counsellor_room_id = models.IntegerField()

    class Meta:
        db_table = 'user'


class Room(models.Model):
    user_count = models.IntegerField()
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'room'


class Counsellor(models.Model):
    counsellor_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    class Meta:
        db_table = 'counsellor'


class CounsellorRoom(models.Model):
    counsellor = models.ForeignKey('Counsellor')
    room = models.ForeignKey('Room')

    class Meta:
        db_table = 'counsellor_room'


class Message(models.Model):
    user = models.ForeignKey('User')
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        db_table = 'message'


class Session(models.Model):
    user_id = models.IntegerField()
    session_id = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'session'

    @staticmethod
    def generate_token(user_id):
        Session.objects.filter(user_id=user_id).update(is_active=False)
        token = Session(user_id=user_id, session_id=str(hashlib.sha1(os.urandom(128)).hexdigest())[:32],
                        created_on=datetime.datetime.now())
        token.save()

        return token.session_id

import subprocess

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

