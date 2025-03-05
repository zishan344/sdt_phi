from django.contrib import admin
from .models import Order,OrderItem,Cart,CartItem 
# # Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  list_display = ['id','user']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['id','user','status']


admin.site.register(OrderItem)
admin.site.register(CartItem)