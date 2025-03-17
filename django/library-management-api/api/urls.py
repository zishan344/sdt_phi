from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet,AuthorViewSet,CategoryViewSet,BorrowRecordViewSet
# from rest_framework_nested import routers
router = DefaultRouter()
router.register('book-category',CategoryViewSet, basename='book-category')
router.register('books',BookViewSet, basename='books')
router.register('author',AuthorViewSet, basename='author')
router.register('borrow_record',BorrowRecordViewSet, basename='borrow_record')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]