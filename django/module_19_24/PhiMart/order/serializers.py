from rest_framework import serializers
from product.models import Product
from order.models import Cart, CartItem, Order,OrderItem 
from order.services import OrderService
from product.serializers import ProductSerializer

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:  # Fix: changed 'meta' to 'Meta'
        model = Product
        fields = ['id', 'name', 'price']

class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    
    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']
        
    def validate_product_id(self, value):  # Fix: moved outside Meta
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"Product id {value} does not exists")
        return value
        
    def save(self, **kwargs):  # Fix: moved outside Meta
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data)
        return self.instance

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"CartItemSerializer initialized with: {args}, {kwargs}")
    
    class Meta:
        model = CartItem  # fixed typo from 'mode' to 'model'
        fields = ["id", 'product', 'quantity', 'total_price']
    
    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price
  
class CartSerializer(serializers.ModelSerializer):
  items = CartItemSerializer(many=True,read_only=True)
  total_price = serializers.SerializerMethodField(method_name = "get_total_price")
  class Meta:
    model = Cart
    fields = ['id','user','items','total_price']
    read_only_fields=['user']
  def get_total_price(self,cart:Cart):
    return sum([item.product.price * item.quantity for item in cart.items.all()])

class UpdateCartItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = CartItem
    fields = ['quantity']
    
class OrderItemSerializer(serializers.ModelSerializer):
  product = SimpleProductSerializer()
  class Meta:
    model = OrderItem
    fields = ['id', 'product', 'price', 'quantity', 'total_price']  # Fix: changed 'field' to 'fields'

class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True)
  class Meta:
    model = Order
    fields = ['id', 'user', 'status', 'total_price', 'created_at', 'items']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("No cart found with this id")
        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError("Cart is empty")
        return cart_id
    
    def create(self,validated_data):
        user_id = self.context.get('user_id')
        cart_id = validated_data['cart_id']
        try:
            order = OrderService.Create_order(user_id = user_id, cart_id = cart_id)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return order
    def to_representation(self, instance):
        return OrderItemSerializer(instance).data

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
    def update(self,instance,validated_data):
        user = self.context['user']
        new_status = validated_data["status"]
        if new_status == Order.CANCELED:
            return OrderService.cancel_order(order=instance,user=user)
        
        if not user.is_staff:
            raise serializers.ValidationError(
                {'detail':'You are not allowed to update this order'}
            )
        return super().update(instance,validated_data)

class EmptySerializer(serializers.Serializer):
    pass