from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category


""" class CategorySerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  description = serializers.CharField()
"""
""" class ProductSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  unit_price = serializers.DecimalField(decimal_places=2, max_digits=10, source = 'price')
  price_with_tax = serializers.SerializerMethodField(method_name ="calculate_tax")
  category = CategorySerializer()
  def calculate_tax(self, product):
    return round(product.price * Decimal(1.1),2)
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    product_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price','stock', 'category','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negative')
        return price

