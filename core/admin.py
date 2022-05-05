from django.contrib import admin
from .models import User, Trip, Log, Comment, Contact, Image


admin.site.register(User)
admin.site.register(Trip)
admin.site.register(Log)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Image)