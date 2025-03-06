# poly --> many (multiple)
# morph --> shape

class Animal:
  def __init__(self,name):
    self.name =name
  def make_sound(self):
    print('animal making some sound')

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    print('mew mew')
  
class Dog(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    print('gew gew')

class Goat(Animal):
  def __init__(self, name):
    super().__init__(name)
  def make_sound(self):
    print('beh beh beh')

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Localshepard')
shepard.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

print('!~~~~~~ animals array loop started ~~~~~~~!')
animals = [don,shepard,mess,less]
for animal in animals:
  animal.make_sound()