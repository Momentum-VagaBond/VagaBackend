from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.forms import CharField
from datetime import date

class User(AbstractUser):
    bio = models.CharField(max_length=300, default=True)
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
    title = models.CharField(max_length=200, default=True)
    location = models.CharField(max_length=150, blank=True)
    duration = models.CharField(max_length=50, default=True)
    
    def __str__(self):
        return self.location


class Log(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_log')
    location = models.CharField(max_length=75)
    latitude = models.FloatField('latitude')
    longitude = models.FloatField('longitude')
    details = models.TextField(max_length=250)

    def __str__(self):
        return self.location



class Comment(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, related_name='log_comments')
    comments = models.TextField(max_length=250)
    date_commented = models.DateTimeField

    def __str__(self):
        return self.comments