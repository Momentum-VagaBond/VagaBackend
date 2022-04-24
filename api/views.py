from django.shortcuts import render
from core.models import User, Trip, Contacts, Log, Comment
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions
from .serializers import UserSerializer, TripSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

# List of all trips
class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class UserListView()

# User profile
class UsersView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserTripListView(ListAPIView):
    serializer_class = TripSerializer
    def get_queryset(self):
        return self.request.user.trips.all()