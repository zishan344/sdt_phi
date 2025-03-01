from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from order.serializers import CartSerializer,CartItemSerializer
from order.models import Cart,CartItem

# Create your views here.


class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializer

  def get_queryset(self):
    return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
