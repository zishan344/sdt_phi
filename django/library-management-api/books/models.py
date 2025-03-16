from django.db import models
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
""" 
model List on books app
1. Category
2. Book
3. Author
4. BorrowRecord
"""

class Author(models.Model):
  """ This is the author model of book  """
  id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
  name = models.CharField(max_length=50)
  biography = models.TextField(null=True, blank=True)
  birth_date = models.DateField()
  def __str__(self):
    return self.name

class Category(models.Model):
  """ This is book category Model"""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
  name = models.CharField(max_length=50)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True, editable=False)
  updated_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.name


class Book(models.Model):
  """ This is book model """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
  title = models.CharField(max_length=50)
  isbn = models.CharField(max_length=50, unique=True, null=True, blank=True)
  author=models.ForeignKey(Author,related_name='book_author', on_delete=models.CASCADE)
  # total_books=models.IntegerField(default=1)
  category = models.ForeignKey(Category, related_name='book_category', on_delete=models.CASCADE)
  available = models.BooleanField(default=False)
  publication_date = models.DateField()
  def __str__(self):
    return self.title

class BorrowRecord(models.Model):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
  book = models.ForeignKey(Book, related_name='borrow_book',on_delete=models.CASCADE)
  member=models.ForeignKey(User,related_name='borrow_book_user',on_delete=models.CASCADE)
  borrow_date = models.DateTimeField(auto_now_add=True, editable=False)
  return_date = models.DateField(null=True, blank=True)
  def __str__(self):
    return f"{self.book} borrowed by {self.member} "
