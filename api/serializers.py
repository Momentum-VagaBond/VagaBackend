from core.models import User, Contacts, Trip, Log, Comment
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model=User
        fields=(
            ''





        )