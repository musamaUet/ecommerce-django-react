from django.urls import path
from base.views import product_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView
# )


urlpatterns = [
    path('products/', product_views.getProducts, name='products'),
    path('product/<str:pk>/', product_views.getProduct, name='product')
]