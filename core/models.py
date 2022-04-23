from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', default=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return self.user

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    location = models.CharField(max_length=150, blank=True)
    date_added = models.DateTimeField

    def __str__(self):
        return self.location


class Log(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_log')
    location = models.CharField(max_length=75)
    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    details = models.TextField(max_length=250)

    def __str__(self):
        return self.log_number



class Comment(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, related_name='log_comments')
    comments = models.TextField(max_length=250)
    date_commented = models.DateTimeField

    def __str__(self):
        return self.comments