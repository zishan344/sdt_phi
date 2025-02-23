from django.urls import path
from product import views

urlpattern = [
  path('<int:pk>/', views.view_specific_category, name = 'view-specific-category')
]