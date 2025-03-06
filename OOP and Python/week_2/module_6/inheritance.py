# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class
 
class Gadget:
  def __init__(self,brand,price,color,origin):
    self.brand = brand
    self.price = price
    self.color = color
    self.origin = origin
  def run(self):
    return f'Running laptop: {self.brand}'


class Laptop:
  def __init__(self,memory,ssd) -> None:
    self.memory = memory
    self.ssd = ssd
  def codings(self):
    return f'learning python and practicing'
class Phone(Gadget):
  def __init__(self,brand,price,color,origin,dual_sim):
    self.dual_sim = dual_sim
    super().__init__(brand,price,color,origin)
  
  def phone_call(self,number,text):
    return f'Sending SMS to: {number} with: {text}'
  def __repr__(self) -> str:
    return  f'phone: {self.brand} {self.price} {self.dual_sim}'
  
class Camera:
  def __init__(self,pixel):
    self.pixel = pixel
  def change_lense(self):
    pass
  
#inheritance
my_phone = Phone('iphone',120000,'Silver','china',True)
# my_phone.phone_call()

print(my_phone.brand)
print(my_phone)
  
