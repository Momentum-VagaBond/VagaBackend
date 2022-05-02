#changes
import geocoder
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.core.mail import send_mail

class User(AbstractUser):

    USER_CREATED_PASSWORD_RETYPE = True
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    traveler = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='travelers')
    bio = models.CharField(max_length=300, default='User has yet to fill in their bio')
    avatar = models.ImageField(blank=True, null=True)

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


audience = [
    ('friends', 'friends'),
    ('family', 'family'),
    ('public', 'public'),
    ('private', 'private'),
]

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', default=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    audience = models.CharField(choices=audience, max_length=30, blank=True, null=True)

    def __str__(self):
        return self.first_name


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=200, default=True)
    location = models.CharField(max_length=150, blank=True)
    begin = models.DateTimeField(blank=False,)
    end = models.DateTimeField(blank=False,)
    followers = models.ManyToManyField(Contacts, related_name='trip_followers')
    
    def start_trip(self):
        return self.logs.filter(start=True).exists()
    
    def __str__(self):
        return self.location


mapbox_token = 'pk.eyJ1IjoiZW1pbHlmbG8iLCJhIjoiY2wyZGRsNG9hMHk0aDNicGR1bjhxZGZmdyJ9.OwfzAfjxswxUss6pTmNVUQ'

reactions = [
    ('thumb-up', 'U+1F44D'),
    ('heart-eyes', 'U+1F60D'),
    ('laughing-crying', 'U+1F602'),
    ('cowboy', 'U+1F920'),
    ('frown', 'U+2639'),
    ('angry', 'U+1F621'),
]

class Log(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs', default=True)
    location = models.CharField(max_length=75, blank=True)
    latitude = models.FloatField('latitude', blank=True, null=True)
    longitude = models.FloatField('longitude', blank=True, null=True)
    details = models.TextField(max_length=250)
    start = models.BooleanField(default=False)
    date_logged = models.DateTimeField(auto_now_add=True)
    reactions = models.CharField(choices=reactions, max_length=20, blank=True)

    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.location, key=mapbox_token)
        g = g.latlng
        self.latitude = g[0]
        self.longitude = g[1]
        return super(Log, self).save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #     g = geocoder.mapbox(self.location, key=mapbox_token, method='reverse')
    #     g = g.latlng
    #     self.latitude = 

class Comment(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE, related_name='log_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments', default=True)
    comments = models.TextField(max_length=250)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments

class Image(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True, null=True)
    log_image = models.ForeignKey(Log, on_delete=models.CASCADE, related_name='log_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_images')

    def __img__(self):
        return self.picture