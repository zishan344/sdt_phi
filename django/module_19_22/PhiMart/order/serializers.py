from rest_framework import serializers
from product.models import Product
from order.models import Cart, CartItem
from product.serializers import ProductSerializer

class SimpleProductSerializer(serializers.ModelSerializer):
  class meta:
    model = Product
    fields = ['id','name','price']

class AddCartItemSerializer(serializers.ModelSerializer):
  product_id = serializers.IntegerField()
  class Meta:
    model = CartItem
    fields = ['product_id','quantity']
    def save(self,**kwargs):
      cart_id = self.context['cart_id']
      product_id = self.validated_data['product_id']
      quantity = self.validated_data['quantity']
      try:
        cart_item = CartItem.objects.get(
          cart_id=cart_id,
          product_id=product_id
        )
        cart_item.quantity += quantity
        self.instance = cart_item.save()
      except CartItem.DoesNotExist:
        self.instance = CartItem.objects.create(
          cart_id = cart_id,
          **self.validated_data
        )
      return self.instance
    def validate_product_id(self,value):
      if not Product.objects.filter(pk = value).exists():
        raise serializers.ValidationError(f"Product id {value} does not exists")
      return value
        


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
  items = CartItemSerializer(many=True,read_only=True)
  total_price = serializers.SerializerMethodField(method_name = "get_total_price")
  class Meta:
    model = Cart
    fields = ['id','user','items','total_price']
  def get_total_price(self,cart:Cart):
    return sum([item.product.price * item.quantity for item in cart.items.all()])


