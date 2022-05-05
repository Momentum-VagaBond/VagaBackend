from django.forms import CharField
from core.models import Image, User, Contacts, Trip, Log, Comment
from rest_framework import serializers




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

class ProfileSerializer(serializers.ModelSerializer):
    class TripProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Trip
    trip = TripProfileSerializer()
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data ):
        trip_data = validated_data.pop('trip')
        user_instance = User.objects.create(**validated_data)
        Trip.objects.create(bio=user_instance,
                            title=CharField,
                            avatar=user_instance.avatar,
                            **trip_data
        )
        return user_instance


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'picture',
            )


class LogSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    log = serializers.ImageField(required=False)
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
            'log',
        )



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
            'subscribers',
            'trip_logs'
        )

    def get_trip_logs(self, instance):
        trip_logs = instance.trip_logs.order_by('-pk')
        return LogSerializer(trip_logs, many=True).data


class LogCommentSerializer(serializers.ModelSerializer):
    log = serializers.ImageField(required=False)
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
            'log'
        )


class SubscribeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = (
            'user',
            'title',
            'location',
            'begin',
            'end',
            'subscribers'
        )