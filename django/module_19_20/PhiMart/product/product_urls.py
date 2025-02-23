from django.urls import path
from product import views

urlpattern = [
  path('<int:id>/',views.view_specific_product, name = 'product-list')
]