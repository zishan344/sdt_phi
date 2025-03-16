from rest_framework import serializers
from books.models import Book,Author,BorrowRecord,Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields= '__all__'
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model=Book
    fields= '__all__'
class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model=Author
    fields= '__all__'
class BorrowRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model=BorrowRecord
    fields= '__all__'
