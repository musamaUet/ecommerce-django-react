from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('products', views.getProducts, name='products'),
    path('product/<int:pk>', views.getProduct, name='product')
]