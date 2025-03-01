from rest_framework import serializers
from product.models import Product
from order.models import Cart, CartItem
from product.serializers import ProductSerializer

class SimpleProductSerializer(serializers.ModelSerializer):
  class meta:
    model = Product
    fields = ['id','name','price']

class CartItemSerializer(serializers.ModelSerializer):
  product = SimpleProductSerializer()
  total_price = serializers.SerializerMethodField(method_name='get_total_price')
  class Meta:
    mode = CartItem
    fields= ["id",'product',
            'quantity','total_price']
  def get_total_price(self,cart_item:CartItem):
    return cart_item.quantity * cart_item.product.price
  
class CartSerializer(serializers.ModelSerializer):
  items = CartItemSerializer(many=True)
  total_price = serializers.SerializerMethodField(method_name = "get_total_price")
  class Meta:
    model = Cart
    fields = ['id','user','items','total_price']
  def get_total_price(self,cart:Cart):
    return sum([item.product.price * item.quantity for item in cart.items.all()])


