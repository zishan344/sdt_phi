from django.urls import path
from product import views

urlpatterns = [
  path('',views.ProductList.as_view(),name="product-list"),
  path('<int:pk>/',views.ViewSpecificProduct.as_view(), name = 'product-details')
]