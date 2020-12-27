from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product


# Create your views here.
def main(request):
    return HttpResponse('test')


class ProductView(generics.ListAPIView): #generics.CreateAPIView 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
