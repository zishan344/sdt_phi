class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")
        super(B, self).show()  # Manually B er parent A call hocche

class C(A):
    def show(self):
        print("C class")
        super(C, self).show()  # Manually C er parent A call hocche

class D(B, C):  # Multiple Inheritance
    def show(self):
        print("D class")
        super(D, self).show()  # Python e MRO (Method Resolution Order) follow korbe

d = D()
d.show()
