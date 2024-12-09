class Library:
  book_list=[]
  @classmethod
  def entry_book(cls,book):
    cls.book_list.append(book)
class Book(Library):
  def __init__(self,book_id,title,author,availability):
    self.__book_id = book_id
    self.__title = title
    self.__author = author
    self.__availability = availability
    self.entry_book(self) 
  def borrow_book(self,book_id):
    found = False
    for book in self.book_list:
      if book.__book_id == book_id:        
        found = True
        if not book.__availability:
          raise ValueError("already borrow this book chose another one")
        else:
          print(f'\nBook "{book.__title}" borrow successfully! \n')
          self.book_list[book_id-1].__availability=False 
          break
    if not found:
      raise ValueError("Invalid Book ID.Not available this book")
    return
  def return_book(self, book_id):
    found = False
    
    for book in self.book_list:
      
      if book.__book_id == book_id:
        found = True
        if book.__availability == True:
          raise ValueError("booked not borrow. it's already available")      
        else:
         print(f'\nBook "{book.__title}" returned successfully! \n')
         self.book_list[book_id-1].__availability=True        
         break
    if not found:      
       raise ValueError("Invalid Book ID.Not available this book")
    return
  def view_book_info(self):
    for book in self.book_list:
     print (f'ID: {book.__book_id}, Title: {book.__title}, Author: {book.__author}, Availability: {"Available"if book.__availability==True else "Not Available"}')


book1 = Book(1, "To Kill a Mockingbird", "Harper Lee", True)
book2 = Book(2, "1984", "George Orwell", True)
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald", True)
book4 = Book(4, "Pride and Prejudice", "Jane Austen", True)
book5 = Book(5, "Moby Dick", "Herman Melville", True)
book6 = Book(6, "War and Peace", "Leo Tolstoy", True)
book7 = Book(7, "The Catcher in the Rye", "J.D. Salinger", True)
book8 = Book(8, "The Lord of the Rings", "J.R.R. Tolkien", True)
book9 = Book(9, "The Alchemist", "Paulo Coelho", True)
book10 = Book(10, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", True)
# print(myBook.view_book_info())


while(True):
  print('\n\n ~~~~Welcome To the Library~~~~~  \n')
  print('1. View All Books')
  print('2. Borrow Book')
  print('3. Return Book')
  print('4. Exit.')
  try:
   val = int(input("Enter your choice: "))
   if val == 1:
        Book.view_book_info(Book)
   elif val == 2:
      try :
        Book.borrow_book(Book,int(input('enter your book id to borrow: ')))
      except ValueError as e:
        print(f'{e}')
   elif val == 3:
      try:
       Book.return_book(Book,int(input('enter your book id to return: ')))
      except ValueError as e:
        print(f'{e}')
   
   elif val == 4:
     break
   else:
     print(f'Invalid input. please choice 1 to 4')
  except ValueError:
    print(f'Invalid input. Please enter a valid integer choice.')
