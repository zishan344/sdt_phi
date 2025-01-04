from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurant import Restaurant
from orders import Order

mamar_restaurant = Restaurant("Mamar Restaurant")

def customer_menu():
  name = input("Enter Your Name : ")
  email = input("Enter Your Email : ")
  phone = input("Enter Your Phone : ")
  address = input("Enter Your Address : ")
  customer = Customer(name=name, email=email, phone=phone, address=address)

  while True:
    print(f"Welcome to {customer.name}!!")
    print("1. View Menu")
    print("2. Add item to cart")
    print("3. View Cart")
    print("4. PayBill")
    print("5. Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
      Customer.view_menu(customer,mamar_restaurant)
    elif choice == 2:
      item_name = input("Enter item name : ")
      item_quantity = int(input("Enter item quantity : "))
      Customer.add_to_cart(customer,mamar_restaurant,item_name,item_quantity)
    elif choice == 3:
      Customer.view_cart(customer)
    elif choice == 4:
      Customer.pay_bill(customer)
    elif choice == 5:
      break
    else:
      print("Invalid Input")

def admin_menu():
  name = input("Enter Your Name : ")
  email = input("Enter Your Email : ")
  phone = input("Enter Your Phone : ")
  address = input("Enter Your Address : ")
  admin = Admin(name = name, email = email, phone = phone, address = address)

  while True:
    print(f"Welcome {admin.name}!!")
    print("1. Add New Item")
    print("2. Add New Employee")
    print("3. View Employee")
    print("4. View Items")
    print("5. Delete Item")
    print("6. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
      item_name = input("Enter Item Name : ")
      item_price = int(input("Enter Item Price : "))
      item_quantity = int(input("Enter Item Quantity : "))
      item = FoodItem(item_name,item_price,item_quantity)
      admin.add_new_item(mamar_restaurant,item)
    elif choice == 2:
      name = input("Enter employee Name : ")
      phone = input("Enter employee phone : ")
      email = input("Enter employee email : ")
      designation = input("Enter employee designation : ")
      age = input("Enter employee age : ")
      salary = input("Enter employee salary : ")
      address = input("Enter employee address : ")
      employee = Employee(name,phone,email,address,age,designation,salary)
      admin.add_employee(mamar_restaurant,employee)
    elif choice == 3:
      admin.view_employee(mamar_restaurant)
    elif choice == 4:
      admin.view_menu(mamar_restaurant)
    elif choice == 5:
      item_name = input("Enter item Name : ")
      admin.remove_item(mamar_restaurant,item_name)
    elif choice ==6:
      break
    else:
      print("Invalid Input")


while True:
  print("Welcome!!")
  print("1. Customer")
  print("2. Admin")
  print("3. Exit")
  choice =int(input("Enter your choice: "))
  if choice == 1:
    customer_menu()
  elif choice == 2:
    admin_menu()
  elif choice == 3:
    break
  else:
    print("Invalid Input!!")