from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product,Review
from django.shortcuts import get_object_or_404
from product.serializers import ProductSerializer, CategorySerializer,ReviewSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from api.permissions import IsAdminOrReadOnly
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


class CategoryViewSet(ModelViewSet):
  
  queryset = Category.objects.annotate(
    product_count=Count('products')
  ).all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_class = ProductFilter
  pagination_class = DefaultPagination
  search_fields = ['name', 'description']
  ordering_fields = ['price', 'updated_at']
  # permission_classes = [IsAdminUser]
  permission_classes = [IsAdminOrReadOnly]
  """ def get_permissions(self):
    if self.request.method == "GET": 
      return [AllowAny()]
    return [IsAdminUser()] """

  
  def destroy(self, request, *args, **kwargs):
    product = self.get_object()
    if product.stock > 10:
      return Response({
        "message": "Product with stock more than 10 could not be deleted"
      })
    self.perform_destroy(product)
    return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet(ModelViewSet):
  serializer_class = ReviewSerializer
  def get_queryset(self):
      return Review.objects.filter(product_id=self.kwargs['product_pk'])
  def get_serializer_context(self):
    return {'product_id':self.kwargs['product_pk']}
  
