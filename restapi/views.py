from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Company
from api.serializers import CompanySerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List': '/company-list/',
        'Detail View':'/company-detail/<str:pk>/',
        'Create':'/company-create/',
        'Update':'/company-update/<str:pk>/',
        'Delete':'/company-delete/<str:pk>/'
    }
    return Response(api_urls)
