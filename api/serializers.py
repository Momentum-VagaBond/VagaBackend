from core.models import User, Contacts, Trip, Log, Comment
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    class Meta:
        model=User
        fields=(
            'id',
            'username',
            'user_first_name',
            'user_last_name',
            'bio',
        )

class TripSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    def get_user(self, obj):
        return obj.user.username
    class Meta:
        model=Trip
        fields=(
            'pk',
            'title',
            'location',
            'duration',
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            #contacts list
        )