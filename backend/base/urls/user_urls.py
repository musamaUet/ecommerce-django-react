from django.urls import path
from base.views import user_views

urlpatterns = [
    path('users/login', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile', user_views.getUserProfile, name='user-profile'),
    path('users/', user_views.getUsers, name='users'),
    path('users/register', user_views.registerUser, name='register'),
]