"""VagaBond URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', api_views.CustomAuthToken.as_view()), # custom login for front end to receive userpk at login
    # path('auth/register/', api_views.CustomRegistrationView.as_view()),

    path('api/auth/me', api_views.UserProfileView.as_view(), name='user-detail'), # my profile
    path('api/trips/', api_views.TripListView.as_view(), name='trip-list'),# list of all trips, all users (so far)
    path('api/mytrips/', api_views.UserTripsView.as_view(), name ='user-trips'), # view all trips created by user or create trips
    path('api/users/<int:pk>/<int:trip_pk>/log/', api_views.TripLogView.as_view(), name='trip-log'), # create a specific log in a trip
    path('api/trips/<int:pk>/', api_views.TripDetailView.as_view(), name='trip-details'), # specific trips with respective logs
    path('api/log/<int:pk>/', api_views.LogDetailView.as_view(), name='log-details'),
    path('api/log/<int:pk>/comment/', api_views.CommentView.as_view(), name='log-comments'),
]

