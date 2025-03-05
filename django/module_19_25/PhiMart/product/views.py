from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from rest_framework.permissions import DjangoModelPermissions
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadonly
from product.models import Category, Product,Review,ProductImage
from product.serializers import ProductSerializer, CategorySerializer,ReviewSerializer,ProductImageSerializer
from drf_yasg.utils import swagger_auto_schema
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
  """ 
  Api endpoint for managing products in the e-commerce store.
  - Allows authenticated admin to create, update, and delete products
  - Allows users to browse and filter product
  - support searching by name, description, and category
  - support ordering by price and update_at
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filterset_class = ProductFilter
  pagination_class = DefaultPagination
  search_fields = ['name', 'description']
  ordering_fields = ['price', 'updated_at']
  permission_classes = [IsAdminOrReadOnly]

  @swagger_auto_schema(operation_summary='Retrieve a list of prodcut')
  def list(self, request, *args, **kwargs):
    """Retrieve all the products"""
    return super().list(request, *args, **kwargs)

  @swagger_auto_schema(
      operation_summary='create Product by admin',
      operation_description= 'This allow an admin to create a product',
      requset_body = ProductSerializer,
      responses = {
        201:ProductSerializer,
        400:"Bad Request"
      }
      )
  def create(self, request, *args, **kwargs):
    """Only authenticated admin can create product"""
    return super().create(request, *args, **kwargs)
class ProductImageViewSet(ModelViewSet):
  serializer_class = ProductImageSerializer
  permission_classes = [IsAdminOrReadOnly]
  def get_queryset(self):
    return ProductImage.objects.filter(product_id = self.kwargs.get('product_pk'))
  
  def perform_create(self,serializer):
    serializer.save(product_id = self.kwargs.get('product_pk'))

class ReviewViewSet(ModelViewSet):
  permission_classes = [IsReviewAuthorOrReadonly]
  serializer_class = ReviewSerializer
  

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
  def perform_update(self, serializer):
    serializer.save(user=self.request.user)
  def get_queryset(self):
      return Review.objects.filter(product_id=self.kwargs.get('product_pk'))
  def get_serializer_context(self):
    return {'product_id':self.kwargs.get('product_pk')}
  
