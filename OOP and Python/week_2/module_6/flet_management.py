# Ena poribohon

class Company:
  def __init__(self,name,address) ->None:
    self.name = name
    self.bus=[]
    self.route=[]
    self.drivers=[]
    self.counter=[]
    self.manager=[]
    self.supervisor=[]
    self.fare=[]
class Driver:
  def __init__(self,name,license,age) -> None:
    self.license=license
    self.name=name
    self.age=age
class Counter:
  def __init__(self) -> None:
    pass
  def purchase_a_ticket(self,start,destination):
    pass
class Passenger:
  pass
class Supervisor:
  pass
red_mia=Driver('a','123',32)

    