
class Product:
  def __init__(self, item_name, description, price, quantity):
    self.item_name = item_name
    self.description = description
    self.price = price
    self.quantity = quantity
     

class Shop(Product):
  def __init__(self):
    self.products=[]
  def add_product(self, product):
    self.products.append(product)
    print(product.item_name)
     
  def buy_product(self,item_name,quantity):
   for product in self.products:
     if product.item_name == item_name:
       if product.quantity >= quantity:
          print(f"Congrats! You bought {quantity} {item_name}(s). Remaining stock: {product.quantity-quantity}.")
          return
       else:
         print(f"Sorry, only {product.quantity} {item_name}(s) are available.")
         return
     else:
       print(f"Sorry, {item_name} is not available in the shop.")
       
       
       
# Create Shop object
my_shop = Shop()

# Create Product objects
laptop = Product("Laptop", "High-performance laptop", 1200, 10)
smartphone = Product("Smartphone", "Latest model smartphone", 800, 20)

# Add products to the shop
my_shop.add_product(laptop)
my_shop.add_product(smartphone)

# Buy products
my_shop.buy_product("Laptop", 2)
my_shop.buy_product("Smartphone", 25)
my_shop.buy_product("Tablet", 1)
