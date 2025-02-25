from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET'])
def view_categories(request):
  categories = Category.objects.annotate(
    product_count = Count('products')).all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

class ViewCategory(APIView):
  def get(self, request):
    categories = Category.objects.annotate(product_count = Count('products')).all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificCategory(APIView):
  def get(self, request, pk):
    category = Category.objects.annotate(
    product_count=Count('products')
  ).get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view()
def view_specific_category(request, pk):
  category = Category.objects.annotate(
    product_count=Count('products')
  ).get(pk=pk)
  serializer = CategorySerializer(category)
  return Response(serializer.data)

""" @api_view(["GET", "POST"])
def view_products(request):
  if request.method == "GET":
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED) """

class ViewProducts(APIView):
  def get(self,request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(
      products,many=True
    )
    return Response(serializer.data)
  def post(self,request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificProduct(APIView):
  def get(self, request, pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  def put(self,request, pk):
    product = get_object_or_404(Product,pk=pk)
    serializer = ProductSerializer(product,data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  def delete(self,request, pk):
    product = get_object_or_404(Product,pk=pk)
    copy_of_product = product
    product.delete()
    serializer = ProductSerializer(copy_of_product)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
""" 
@api_view(['GET','PUT','DELETE'])
def view_specific_product(request,pk):
  if request.method == 'GET':
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  elif request.method == 'PUT':
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product,data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    product.delete()
    return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
"""

  
