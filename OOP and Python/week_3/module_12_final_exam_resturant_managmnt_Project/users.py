
class Restaurant:
  food_menu =[] 
  customers = []
  @classmethod
  def showMenu(self):
    if len(self.food_menu) == 0:
      print("menu is empty")
    else:
      print("~~~Restaurant Menu!!~~~")
      for item in self.food_menu:
        print(f"foodId: {item.id}, name : {item.name}, price : {item.price}, quantity : {item.quantity}")
  @classmethod
  def add_food(self,food):
    self.food_menu.append(food)
    print("food added successfully!!")
  @classmethod
  def remove_food(self,id):
    found = False
    for f in self.food_menu:
      if f.id == id:
        found = True
        self.food_menu.remove(f)
        break
    if found:
      print("Yay!! your selected food removed successfully")
    else:
      print("Your selected food item not available")
 
  @classmethod
  def customer_details(self):
    print("view all customers")
    print("id \t name \t email \t\t\t  address")
    for cus in self.customers:
      print("%s \t %s \t %s \t\t\t  %s"%(cus.id,cus.name, cus.email, cus.address))

class FoodObj(Restaurant):
  def __init__(self,name,price,quantity):
    super().__init__()
    self.id = len(self.food_menu)+1 if len(self.food_menu) == 0 else self.food_menu[-1].id+1
    self.name = name
    self.price = price
    self.quantity = quantity

class OrderObj:
  def __init__(self,order_id,name,total_price,quantity):
    self.order_id = order_id
    self.name = name
    self.total_price = total_price
    self.quantity = quantity
class Customer(Restaurant): 
  def __init__(self,name,email,address):
    super().__init__()
    # if id:
    #   self.id = id
    # else:
    #  self.id = len(self.customers)+1 if len(self.customers) == 0 else self.customers[-1].id+1
    self.id = len(self.customers)+1 if len(self.customers) == 0 else self.customers[-1].id+1  
    self.name = name
    self.email = email
    self.address = address
    self.orders = []
    self.__balance = 0

  def restaurant_menu(self):
    self.showMenu()
  def place_order(self,order_id,itemID,order_quantity):
    if len(self.food_menu)==0:
      print ("not available any food")
      return
    found = False
    blLow = False
    qnLow = False
    for item in self.food_menu:
      if item.id==itemID:
        found = True
        totalPrice= item.price * order_quantity
        if item.quantity >= order_quantity:
         if self.__balance >= totalPrice:
          foodName=item.name
          totalPrice= totalPrice
          self.__balance -=totalPrice
          item.quantity -= order_quantity
          newOrder = OrderObj(order_id,foodName,totalPrice,order_quantity)
          self.orders.append(newOrder)
          print(f"successfully completed your order. your remaining balance {self.__balance}")
          break
         else:
           blLow = True
           break
        else:
          qnLow = True
          break
    if not found:
      print("product not available")
    elif found and qnLow:
      print("food quantity not available")
    elif found and blLow:
          print("Oops You Don't have a sufficient balance please add fund and order again.")
  
  def past_orders_list(self):
    if len(self.orders) == 0:
      print("You have no orders to show")
    else:
      print("~~~view your past orders~~~")
      for order in self.orders:
        print(f"name: {order.name}, price: {order.total_price}, quantity: {order.quantity}")
  def check_balance(self):
    print(f"Your available balance {self.__balance}")
  def add_fund(self,amount):
    self.__balance +=amount
    print(f"yay!! successfully added {amount} tk.\n your new balance {self.__balance}")


class Admin(Restaurant):
  def __init__(self,name):
    super().__init__()
    self.name = name

  def create_an_customer(self, customer):  
    self.customers.append(customer)
    return "Yay!! customer created successfully"
   
  
  def remove_customer_account(self, custId):
    found = False
    for customer in self.customers:
      if customer.id == custId:
        found = True
        self.customers.remove(customer)
        break
    if not found:
      print("Your selected customer account are not available")
    else:
      print("Yay!! your selected customer account removed successfully")
  def add_menu(self,id,name,price):
    food = {id,name,price}
    self.add_food(food)
  def remove_menu(self,id):
    self.remove_food(id)
  
  def view_restaurant_menu(self):
    self.showMenu()
    
  def view_all_customers(self):
    self.customer_details()
  def update_price(self, itemId,newPrice):
    if len(self.food_menu) == 0:
      print("food menu is empty you can't update any price")
      return
    found = False
    for f in self.food_menu:
      if f.id == itemId:
        f.price = newPrice
        found = True
        break
    if not found:
      print("item not found for update price")
    else:
      print("update price successfully!!")    
      

    
# starting loop
def optionInput(flag, desc=any):
  try:
   if flag:
    op = int(input(f"{desc} : "))
   else:
     op = input(f"{desc} : ")
   return op
  except ValueError:
    return ValueError


while True:
  print("~~~Restaurant management system~~~")
  print("1. Admin Login")
  print("2. customer login")
  print("3. Exit")
  op = optionInput(True,"select an option")
  if op == 1:
    adName =optionInput(False,"Enter Admin Name")
    admin  = Admin(adName)
    print(f"\nWelcome to Admin-> {adName}.\n")
    print("~~~Admin Menu~~~~\n")
    while True:
      print("1. Create customer account")
      print("2. Remove customer account")
      print("3. View All customers")
      print("4. manage restaurant menu")
      print("5. Exit")
    
      op = optionInput(True,"select an option")
      if op == 1:
        name = optionInput(False,"Enter you name")
        email = optionInput(False,"Enter you email")
        address = optionInput(False,"Enter you address")
        newCustomer = Customer(name,email,address)
        createCustomer = admin.create_an_customer(newCustomer)
        print(createCustomer)
      elif op == 2:
        custId = optionInput(True,"Enter removed customer ID")
        admin.remove_customer_account(custId)
        continue
      elif op == 3:
        admin.view_all_customers()
      elif op == 4:
       print("~~~~Manage restaurant menu~~~~")
       while True:
         print("1. add menu item")
         print("2. remove menu item")
         print("3. view menu item")
         print("4. update food price")
         print("5. Exit")
         op = optionInput(True, "Select an option")
         if op == 1:
           name = input("Enter Item Name : ")
           price = float(input("Enter Item Price : "))
           quantityItem = int(input("Enter Item Quantity : "))
           newItem =FoodObj(name,price,quantityItem)
           admin.add_food(newItem)
         elif op == 2:
           food_id = optionInput(True,"Enter your food id")
           admin.remove_food(food_id)
         elif op == 3:
           print("~~~~~~Food Menu~~~~~~~\n")
           admin.showMenu()
         elif op == 4:
            food_id = optionInput(True,"Enter your updated Price food id")
            new_price = float(input("Enter your new Price : "))
            admin.update_price(food_id, new_price)
         elif op == 5:
           break
         else:
           print("~~~~Invalid input~~~~")
      elif op == 5:
        break
      else:
        print("~~~~Invalid input~~~~")

  elif op == 2:
    username =optionInput(False,"Enter customer username")
    myRestaurant = Restaurant()
    found = False
    myCustomer = {}
    for cus in myRestaurant.customers:
      if cus.name == username:
        myCustomer=cus
        found = True
        break
    if found:
      print(f"\nWelcome to customer-> {username}.\n")
      print("~~~Customer Menu~~~~\n")
      # id, name, email, address = myCustomer.values()
      # print(f"{id} {name} {email} {address}")
      # newCustomer = Customer(name,email,address,id)
      while True:
       print("1. view Restaurant Menu")
       print("2. View Balance")
       print("3. Add Balance")
       print("4. Place Order")
       print("5. View past orders")
       print("6. Exit")
       op = optionInput(True,"Select an option")
       if op ==1:
         myCustomer.restaurant_menu()
       elif op ==2:
         myCustomer.check_balance()
       elif op ==3:
         newFound = optionInput(True,"Enter amount")
         myCustomer.add_fund(newFound)
       elif op ==4:
         itemId = optionInput(True,"Enter food id")
         order_quantity = optionInput(True,"Enter Quantity")
         order_id=len(myCustomer.orders)+1 if len(myCustomer.orders) == 0 else myCustomer.orders[-1].order_id+1
         myCustomer.place_order(order_id,itemId,order_quantity)
       elif op ==5:
         myCustomer.past_orders_list()
       elif op ==6:
         break
       else:
         print("~~~~Invalid input~~~~")
    else:
      print("You don't have any account")
  elif op == 3:
    print("Are you sure? y/n")
    op = optionInput(False,"Select an option")
    if op == "y":
      print("\n~~~~~~Successfully stop your program~~~~~~\n")
      break
    else:
      continue
  else:
    print("Please enter the correct option")
