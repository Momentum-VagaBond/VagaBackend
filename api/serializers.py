from core.models import Image, User, Contacts, Trip, Log, Comment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    trips = serializers.SerializerMethodField

    class Meta:
        model=User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'bio',
            'trips',
        )


class ContactsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Contacts
        fields = (
            'user',
            'first_name',
            'last_name',
            'email',
        )


class TripContactsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Contacts
        fields = (
            
        )


class TripSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    trip_logs = serializers.SerializerMethodField()

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
            'trip_logs'
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'picture',
            'log_images',
            'user_images',
            'uploaded_at',
        )


class LogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    start_trip = serializers.SerializerMethodField()
    log_images = serializers.ImageField(required=False)
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
            'date_logged',
            'reactions',
            'log_images',
        )
    def start_trip(self, obj):
        return obj.start_trip()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')

    def get_user(self, obj):
        return obj.user.username

    def get_user_comments(self, obj):
        return obj.user_comments

    class Meta:
        model = Comment
        fields = (
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            'comments',
            'date_commented',
        )


class TripLogSerializer(serializers.ModelSerializer):
    trip_logs = serializers.SerializerMethodField()
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
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            'trip_logs'
        )

    def get_trip_logs(self, instance):
        trip_logs = instance.trip_logs.order_by('-pk')
        return LogSerializer(trip_logs, many=True).data


class LogCommentSerializer(serializers.ModelSerializer):
    log_images = serializers.ImageField(required=False)
    log_comments = CommentSerializer(many=True, required=False)
    user = serializers.SerializerMethodField()

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
            'date_logged',
            'reactions',
            'log_comments',
            'log_images'
        )