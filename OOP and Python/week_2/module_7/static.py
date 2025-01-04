# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# differences between static method and class method

class Shopping:
  cart=[] # class attribute  #static attribute
  origin='china'

  def __init__(self, name, location):
    self.name = name
    self.location = location
  def purchase(self,item,price,amount):
    remaining = amount - price
    print(f'buying: {item} for price: {price} and remaining : {remaining}')

  
  @staticmethod
  def multiply(a,b):
    result = a * b
    print(result)

  @classmethod
  def hudai_dekhi(self,item):
    print(self.__name__)
    print('hudai deklam kinto kinmo na just ac are hawa kaite aslam',item)

basundara = Shopping('basu en dara', 'not popular location')
basundara.purchase('lungi',500,1000)
# basundara.hudai_dekhi('lungi')
#Shopping.purchase(2,3,3)

#static method
Shopping.multiply(4,6) 

# basundara.multiply(6,9)


