from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import Product2,Product1,Product3,Product4
from restapi.serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'shoe-List': '/prod1-list/',
        'anarkali-List':'/prod2-list/',
        'spec-List':'/prod3-list/',
        'hoodie-List':'/prod4-list/',
    }
    return Response(api_urls)
@api_view(['GET'])
def prod1(request):
    prod1 = Product1.objects.all()
    serializer = ProductSerializer(prod1, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def prod2(request):
    prod2 = Product2.objects.all()
    serializer = ProductSerializer(prod2, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def prod3(request):
    prod3 = Product3.objects.all()
    serializer = ProductSerializer(prod3, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def prod4(request):
    prod4 = Product4.objects.all()
    serializer = ProductSerializer(prod4, many = True)
    return Response(serializer.data)
