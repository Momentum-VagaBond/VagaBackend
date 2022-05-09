from django.forms import CharField
from core.models import Image, User, Contact, Trip, Log, Comment
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Contact
        fields = (
            'user',
            'first_name',
            'last_name',
            'email',
        )



class ImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = (
            'picture',
            )



class TripSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    

    def get_user(self, obj):
        return obj.user.username

    def get_trip_logs(self, obj):
        return obj.trip_logs

    class Meta:
        model = Trip
        fields = (
            'pk',
            'title',
            'location',
            'begin',
            'end',
            'subscribers',
            'user',
            'username',
            'user_first_name',
            'user_last_name',
            
            
            
        )



class UserSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True, read_only=True)
    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')
    
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



class LogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    images = ImageSerializer(required=False, many=True)

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Log
        fields = (
            'pk',
            'user',
            'title',
            'location',
            'latitude',
            'longitude',
            'details',
            'date_logged',
            'reactions',
            'images',
        )



# nest image serializer inside log serializer and return picture



class CommentSerializer(serializers.ModelSerializer):

    username = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user')
    user_first_name = serializers.SlugRelatedField(slug_field='first_name', read_only='True', source='user')
    user_last_name = serializers.SlugRelatedField(slug_field='last_name', read_only='True', source='user')

    # def get_user(self, obj):
    #     return obj.instance.user.username

    # def get_user_comments(self, obj):

    #     return obj.user_comments

    class Meta:
        model = Comment
        fields = (
            
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
    images = ImageSerializer(required=False, many=True)

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
            'subscribers',
            'trip_logs',
            'images',
        )

    def get_trip_logs(self, instance):
        trip_logs = instance.trip_logs.order_by('-pk')
        return LogSerializer(trip_logs, many=True).data



class LogCommentSerializer(serializers.ModelSerializer):
    images = ImageSerializer(required=False, many=True)
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
            'title',
            'latitude',
            'longitude',
            'details',
            'date_logged',
            'reactions',
            'log_comments',
            'images'
        )



class SubscribeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    trip_subscribers = serializers.SerializerMethodField()
    
    class Meta:
        model = Contact
        fields = (
            'user',
            'title',
            'location',
            'begin',
            'end',
            'subscribers',
            'trip_subscribers'
        )



class LogCommentImageSerializer(serializers.ModelSerializer):
    images = ImageSerializer(required=False, many=True)
    log_comments = CommentSerializer(required=False, many=True)

    class Meta:
        model = Log
        fields = (
            'pk',
            'title',
            'location',
            'latitude',
            'longitude',
            'details',
            'date_logged',
            'reactions',
            'images',
            'log_comments',
        )
