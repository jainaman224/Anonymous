from django.db import models


# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
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
    counsellor_id = models.IntegerField()
    room_id = models.IntegerField()

    class Meta:
        db_table = 'counsellor_room'
