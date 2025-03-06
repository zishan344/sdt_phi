#  calculator class to do add, deduct, multiply, divide

class Calculator:
    def add(self,a,b):
        return a + b
    def deduct(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        return a / b

clac=Calculator()
print(clac.add(10,20))
print(clac.deduct(20,10))
print(clac.multiply(10,20))
print(clac.divide(20,10))