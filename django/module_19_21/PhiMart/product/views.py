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
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# import ModelViewSet


# Create your views here.
""" @api_view(['GET'])
def view_categories(request):
  categories = Category.objects.annotate(
    product_count = Count('products')).all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data) """

class ViewCategorys(APIView):
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
  def put(self,request,pk):
    category = get_object_or_404(Category.objects.annotate(product_count=Count('products')),
    pk=pk)
    serializer = CategorySerializer(category,data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  def delete(self, request, pk):
    category = get_object_or_404(
      Category.objects.annotate(product_count=Count('products')),
      pk=pk
    )
    copy_of_category = category
    category.delete()
    serializer = CategorySerializer(copy_of_category)
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

""" @api_view()
def view_specific_category(request, pk):
  category = Category.objects.annotate(
    product_count=Count('products')
  ).get(pk=pk)
  serializer = CategorySerializer(category)
  return Response(serializer.data) """

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

""" class ViewProducts(APIView):
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

"""
class ProductList(ListCreateAPIView):
  queryset = Product.objects.select_related('category').all()
  serializer_class = ProductSerializer
  """def get_queryset(self):
    return Product.objects.select_related('category').all()

  def get_serializer_class(self):
    return ProductSerializer """
  

class ProductDetails(RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  """ override delete method """
  def delete(self,request,pk):
    product = get_object_or_404(Product,pk=pk)
    if product.stock > 10:
      return Response({
        "message": "Product with stock more than 10 could not be deleted"
      })
    product.delete()
    return Response({
      "message": "Product deleted successfully"
    },status=status.HTTP_204_NO_CONTENT)
    
  """ if not write pk should be need at this time lookup_field """
  # lookup_field = 'id'

class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.annotate(
    product_count=Count('products')
  ).all()
  serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def destroy(self, request, *args, **kwargs):
    product = self.get_object()
    if product.stock > 10:
      return Response({
        "message": "Product with stock more than 10 could not be deleted"
      })
    self.perform_destroy(product)
    return Response(status=status.HTTP_204_NO_CONTENT)


""" 
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

  
