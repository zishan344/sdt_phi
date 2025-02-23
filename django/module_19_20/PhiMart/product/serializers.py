from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category

class ProductSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  unit_price = serializers.DecimalField(decimal_places=2, max_digits=10, source = 'price')
  price_with_tax = serializers.SerializerMethodField(method_name ="calculate_tax")

  def calculate_tax(self, product):
    return round(product.price * Decimal(1.1),2)
  