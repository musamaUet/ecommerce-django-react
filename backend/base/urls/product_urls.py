from django.urls import path
from base.views import product_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('/', product_views.getProducts, name='products'),
    path('/<str:pk>/', product_views.getProduct, name='product')
]