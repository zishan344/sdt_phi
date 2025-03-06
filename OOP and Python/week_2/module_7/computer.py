# inheritance vs composition

class CPU:
  def __init__(self,cores):
    pass

class RAM:
  def __init__(self,size):
    self.size = size
class HardDrive:
  def __init__(self,capacity):
     self.capacity = capacity

# computer has a cpu
# computer has a ram
# computer has a hard drive

class Computer:
  def __init__(self,cores,ram_size,hd_capacity):
    self.cpu = CPU(cores)
    self.ram=RAM(ram_size)
    self.hard_disk=HardDrive(hd_capacity)
mac = Computer(8,16,512);
print()