from rest_framework.viewsets import ModelViewSet
from books.models import Book, Author, BorrowRecord, Category
from books.serializers import BookSerializer, AuthorSerializer, BorrowRecordSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from books.permissions import IsLibrarian

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsLibrarian()]
        return [IsAuthenticated()]
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsLibrarian] 

class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update']:
            return [IsAuthenticated()]
        if self.action in ['destroy']:
            return [IsAuthenticated(), IsLibrarian()]
        return [IsAuthenticated()]
