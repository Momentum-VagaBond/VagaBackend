from django.shortcuts import get_object_or_404
from core.models import User, Trip, Contacts, Log, Comment
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions
from .serializers import LogCommentSerializer, UserSerializer, TripSerializer, LogSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from api import serializers

# List of all trips
class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# User profile
class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# Specific user's trip list
class UserTripListView(ListAPIView):
    serializer_class = TripSerializer
    def get_queryset(self):
        return self.request.user.trips.all()

# Log an entry on a trip
class TripLogView(ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    def perform_create(self, serializer):
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, trip=trip)
        return Log(serializer.data)

class LogCommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = LogCommentSerializer
    # def get_queryset(self):
    #     return self.request.user.user_comments['pk']

    def perform_create(self, serializer):
        log = get_object_or_404(Log, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, log=log)
        
