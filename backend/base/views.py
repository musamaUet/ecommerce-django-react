from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/products','/api/products/<id>', '/api/products/create', '/api/products/all']
    return Response(routes)