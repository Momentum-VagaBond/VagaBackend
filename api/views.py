from django.shortcuts import get_object_or_404
from core.models import User, Trip, Contacts, Log, Comment
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import permissions
from .serializers import LogCommentSerializer, UserSerializer, TripSerializer, LogSerializer, TripLogSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from api import serializers

# Profile page
class UserProfileView(ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        return self.request.user.travelers.all()

# Create a new trip with POST, List of all trips with GET
class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Log an entry on a trip
class TripLogView(ListCreateAPIView):
    def get_queryset(self):
        return self.request.user.trips.all()
    serializer_class = TripSerializer
    def perform_create(self, serializer):
        trip = get_object_or_404(Trip, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, trip=trip)
        return Log(serializer.data)

#Comment on a log
class LogCommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = LogCommentSerializer
    def perform_create(self, serializer):
        log = get_object_or_404(Log, pk=self.kwargs["pk"])
        serializer.save(user=self.request.user, log=log)
        
# Specific user and their trips
class UserTripsView(ListCreateAPIView):
    serializer_class = TripSerializer
    def get_queryset(self):
        return self.request.user.trips.all()


# Trips with associated logs -- this is throwing an error "Expected view TripDetailView to be called with a URL keyword argument named "pk". Fix your URL conf, or set the `.lookup_field` attribute on the view correctly."
# However, using breakpoint shows what we are wanting to see, which is the ONE trip and logs associated with the user.
class TripDetailView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripLogSerializer

    # def get_queryset(self):
    #     return get_object_or_404(Trip, pk=self.kwargs["pk"])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)







# # Specific user's trip list
# class UserTripListView(ListAPIView):
#     serializer_class = TripSerializer
#     def get_queryset(self):
#         return self.request.user.trips.all()