
from rest_framework.viewsets import  ModelViewSet
from books.models import Book,Author,BorrowRecord,Category
from books.serializers import BookSerializer,AuthorSerializer,BorrowRecordSerializer,CategorySerializer
# Create your views here.

class BookViewSet(ModelViewSet):
  queryset=Book.objects.all()
  serializer_class=BookSerializer
  
class AuthorViewSet(ModelViewSet):
  queryset=Author.objects.all()
  serializer_class=AuthorSerializer

class BorrowRecordViewSet(ModelViewSet):
  queryset=BorrowRecord.objects.all()
  serializer_class=BorrowRecordSerializer
class CategoryViewSet(ModelViewSet):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer