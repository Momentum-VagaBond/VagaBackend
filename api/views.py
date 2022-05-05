from django.shortcuts import get_object_or_404
from core.models import User, Trip, Contacts, Log, Comment, Image
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions, viewsets
from .serializers import LogCommentSerializer,ProfileSerializer, SubscribeSerializer, UserSerializer, TripSerializer, LogSerializer, TripLogSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from api import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from djoser.views import UserViewSet as DjoserUserViewSet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.timezone import now
from django.template.loader import render_to_string
from .permissions import IsTripOwner


# custom login for the front end to get userpk when logging in [POST]
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'last_login': user.last_login,
            'email': user.email,
            'bio': user.bio
        })

# Profile page [GET]
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Create a new trip with [POST], List of all trips [GET]
class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        #ADD FOLLOWERS query for contacts for logged in user. which ones are you adding? do you want to use the audience feature? make it an optional field on the serializer or query params (which set of contacts do you want to add?) query for 
        # who they are and it's different because it's using ManyToMany i.e. instance - trip.followers.add(queryset(contacts))

# Specific user and their trips [GET]
class UserTripsView(ListCreateAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return self.request.user.trips.all()


class SubscriberView(ListCreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Trip.objects.all()

#     def get_queryset(self):
#         """
#         Get the list of items for this view.
#         This must be an iterable, and may be a queryset.
#         Defaults to using `self.queryset`.

#         This method should always be used rather than accessing `self.queryset`
#         directly, as `self.queryset` gets evaluated only once, and those results
#         are cached for all subsequent requests.

#         You may want to override this if you need to provide different
#         querysets depending on the incoming request.

#         (Eg. return a list of items that is specific to the user)
#         """

#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             # Ensure queryset is re-evaluated on each request.
#             queryset = queryset.all()
#         return queryset


# Log an entry on a trip [POST]
class TripLogView(ListCreateAPIView):
    serializer_class = LogSerializer
    queryset = Trip.objects.all()


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        # is example of what could be used in 'GET' request
        # if self.request.method == 'GET':
        #     self.permission_classes = [IsAuthenticated]
        if self.request.method == 'POST':
            self.permission_classes = [IsTripOwner]
        return self.permission_classes


    def get_queryset(self):
        return self.request.user.trips.all()


    def perform_create(self, serializer):
        trip = get_object_or_404(Trip, pk=self.kwargs["trip_pk"])
        serializer.save(user=self.request.user, trip=trip)
        self.mail_trip_followers()
        


    def mail_trip_followers(self):
        send_mail( 
            'Hello',
            'Body', 
            settings.EMAIL_HOST_USER,
            [settings.RECIPIENT_ADDRESS],
            html_message = render_to_string('mail/log.html', {'greeting':'hello from kpt'})
        )
        


# Trips with associated logs [GET]
class TripDetailView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripLogSerializer

# Log detail page [GET]
class LogDetailView(RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogCommentSerializer

# Comment on a log [POST]
class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        log = get_object_or_404(Log, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, log=log)

# Upload pictures to S3 [POST]
class PictureUploadView(CreateView):
    model = Image 
    fields = ['upload',]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context

# Current active trip for logged in user [GET]
class CurrentActiveView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(end__gt=now().date(), begin__lte=now().date(), user=user)

# Future trips for a logged in user [GET]
class FutureActiveView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(begin__gte=now().date(), user=user)

# Past trips for a logged in user [GET]
class PastActiveView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(end__lte=now().date(), user=user)

# Current trip for users 'im' following
# class CurrentFollowingView(ListCreateAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer
#     def get_queryset(self):
#         user = self.request.following
#         return Trip.objects.filter(end__gt=now().date(), begin__lte=now().date(), user=user)

# Future trips for users 'im' following
# class FutureFollowingView(ListCreateAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer
#     def get_queryset(self):
#         user = self.request.following
#         return Trip.objects.filter(begin__gte=now().date(), user=user)

# Past trips for users 'im' following
# class PastFollowingView(ListCreateAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer
#     def get_queryset(self):
#         user = self.request.following
#         return Trip.objects.filter(end__lte=now().date(), user=user)