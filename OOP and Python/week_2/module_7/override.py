class Person:
  def __init__(self,name,age,height,weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
  def eat(self):
    print("eating something...")
  def exercise (self):
    raise NotImplementedError()
  
class Cricketer(Person):
  def __init__(self, name, age, height, weight,team):
    self.team = team
    super().__init__(name, age, height, weight)
  # override
  def eat(self):
    print('vegetables')
  def exercise(self):
    print('doing workout')
  # + sign operator overload
  def __add__(self, other):
    return self.age + other.age
  # * sign operator overload
  def __mul__(self, other):
    return self.weight * other.weight
  # len overload
  def __len__(self):
    return self.height
  # > overload
  def __gt__(self, other):
    return self.age > other.age
  
sakib = Cricketer('sakib',38,68,91,'BD')
mushi = Cricketer('mushi',36,65,78,'BD')
 

# sakib.eat()
# sakib.exercise()
print (sakib + mushi)
print (sakib * mushi)
print (sakib > mushi)