class Engine:
  def __init__(self):
    pass
  def start(self):
    pass
class Driver:
  def __init__(self):
    pass
# Car has an engine
class Car:
  def __init__(self):
    self.engine = Engine()
    self.driver = Driver()
  def start(self):
    self.engine.start()

