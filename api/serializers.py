from core.models import User, Contacts, Trip, Log, Comment
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    trips = serializers.HyperlinkedIdentityField(view_name='my-trips', format='html')
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
            'trips',
        )