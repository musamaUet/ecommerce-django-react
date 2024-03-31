from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile', views.getUserProfile, name='user-profile'),
    path('products/', views.getProducts, name='products'),
    path('product/<str:pk>/', views.getProduct, name='product')
]