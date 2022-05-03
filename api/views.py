from django.shortcuts import get_object_or_404
from core.models import User, Trip, Contacts, Log, Comment, Image
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions, viewsets
from .serializers import LogCommentSerializer,ProfileSerializer, UserSerializer, TripSerializer, LogSerializer, TripLogSerializer, CommentSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from api import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from djoser.views import UserViewSet as DjoserUserViewSet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.utils.timezone import now


# custom login for the front end to get userpk when logging in
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

# Profile page
class UserProfileView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Create a new trip with POST, List of all trips with GET
class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Specific user and their trips
class UserTripsView(ListCreateAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return self.request.user.trips.all()

# Log an entry on a trip
class TripLogView(ListCreateAPIView):
    def get_queryset(self):
        return self.request.user.trips.all()
    serializer_class = LogSerializer

    def perform_create(self, serializer):
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, trip=trip)
        return Log(serializer.data)

# Trips with associated logs
class TripDetailView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripLogSerializer

# Log detail page
class LogDetailView(RetrieveAPIView):
    queryset = Log.objects.all()
    serializer_class = LogCommentSerializer

# Comment on a log
class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        log = get_object_or_404(Log, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, log=log)

# Upload pictures to S3
class PictureUploadView(CreateView):
    model = Image 
    fields = ['upload',]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context

# Current active trip for logged in user
class CurrentActiveView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(end__gt=now().date(), begin__lte=now().date(), user=user)

# Future trips for a logged in user
class FutureActiveView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(begin__gte=now().date(), user=user)

# Past trips for a logged in user
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