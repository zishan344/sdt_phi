from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count

# Create your views here.
@api_view()
def view_categories(request):
  categories = Category.objects.annotate(
    product_count = Count('products')).all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

@api_view()
def view_specific_category(request, pk):
  category = Category.objects.annotate(
    product_count=Count('products')
  ).get(pk=pk)
  serializer = CategorySerializer(category)
  return Response(serializer.data)

@api_view()
def view_products(request):
  products = Product.objects.select_related('category').all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

@api_view()
def view_specific_product(request,pk):
  product = get_object_or_404(Product, pk=pk)
  serializer = ProductSerializer(product)
  return Response(serializer.data)
