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
        model = Trip
        fields = (
            'pk',
            'title',
            'location',
            'begin',
            'end',
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            #contacts list
        )

class LogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    start_trip = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Log
        fields = (
            'pk',
            'user',
            'location',
            'latitude',
            'longitude',
            'details',
            'start',
        )
    def start_trip(self, obj):
        return obj.start_trip()



class LogCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = (
            'user',
            'comments',
            'date_commented',
        )



class TripLogSerializer(serializers.ModelSerializer):
    trip_logs = LogSerializer(many=True, required=False, source='logs')
    user = serializers.SerializerMethodField()
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Trip
        fields = (
            'trip_pk',
            'title',
            'location',
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            'trip_logs'
        )