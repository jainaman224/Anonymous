import hashlib
import os

import datetime
from django.db import models


# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
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
    room = models.ForeignKey('Room')
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

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
