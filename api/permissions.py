from rest_framework import permissions
from core.models import Trip
from django.shortcuts import get_object_or_404

class IsTripOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a Trip to add a Log.
    """
    def has_permission(self, request):
        trip = get_object_or_404(Trip, pk=request.kwargs["trip_pk"])
        return trip.user.pk == self.user.pk
        
    def has_object_permission(self, request, obj):
        return obj.user == request.user