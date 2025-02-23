from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer

# Create your views here.

def view_specific_category(request):
  pass
@api_view()
def view_specific_product(request,pk):
  product = get_object_or_404(Product, pk=pk)
  serializer = ProductSerializer(product)
  return Response(serializer.data)
