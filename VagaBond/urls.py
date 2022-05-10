from django.contrib import admin
from django.urls import path, include
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls), # backend view of data
    path('api-auth/', include('rest_framework.urls')), # Django REST framework
    path('auth/', include('djoser.urls')), # Djoser authentication
    path('auth/', include('djoser.urls.authtoken')), # token login feature
    path('api-token-auth/', api_views.CustomAuthToken.as_view()), # custom login for front end to receive userpk at login
    path('api/auth/me', api_views.UserProfileView.as_view(), name='user-detail'), # logged in users profile
    path('api/trips/', api_views.TripListView.as_view(), name='trip-list'),# list of all trips, all users (so far), create trips
    path('api/mytrips/', api_views.UserTripsView.as_view(), name='user-trips'), # view all trips created by user
    path('api/users/<int:pk>/<int:trip_pk>/log/', api_views.TripLogView.as_view(), name='trip-log'), # create a specific log in a trip
    path('api/logs/<int:pk>/images/', api_views.PictureUploadView.as_view(), name='picture-upload'),
    path('api/trips/<int:pk>/', api_views.TripDetailView.as_view(), name='trip-details'), # specific trips with respective logs
    path('api/log/<int:pk>/', api_views.LogCommentImageView.as_view(), name='image-log'), # log with pic and comments
    path('api/log/<int:pk>/comment/', api_views.CommentView.as_view(), name='log-comments'), # add/view comments on logs
    path('api/trips/current/user/', api_views.CurrentActiveView.as_view(), name='user-active-trips'), # view current/active trips for logged in user
    path('api/trips/future/user/', api_views.FutureActiveView.as_view(), name='user-future-trips'), # view future trips for logged in user
    path('api/trips/past/user/', api_views.PastActiveView.as_view(), name='user-past-trips'), # view past trips for logged in user
    path('api/contacts/', api_views.UserContactView.as_view(), name='contacts'), # add and view contacts of a user
    path('api/user/subscribed/', api_views.UserSubView.as_view(), name='subscribed'), # view all trips logged in user is subscribed to
    path('api/user/current/subscribed/', api_views.UserCurrentSubView.as_view(), name='current-subscribed'), # view of trips currently taking place the user is subscribed to
    path('api/user/past/subscribed/', api_views.UserPastSubView.as_view(), name='past-subscribed'), # view past trips logged in user is subscribed to
    path('api/user/future/subscribed/', api_views.UserFutureSubView.as_view(), name='future-subscribed'), # view future trips logged in user is subscribed to
]