from django.urls import path, include
# import response
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet
# from rest_framework_nested import routers
router = DefaultRouter()
router.register('books',BookViewSet, basename='books')

urlpatterns = [
    path('',include(router.urls)),
]