import math
import time

def timer(func):
  def inner(*args,**kwargs):
    print("time started")
    start = time.time()
    # print(func)
    func(*args,**kwargs)
    print("time ended")
    end = time.time()
    print(f'total time taken{end-start}')
  return inner

timer(1)()