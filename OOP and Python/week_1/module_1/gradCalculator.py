"""
A: 90 and above
B: 80-89
C: 70-79
D: 60-69
F: below 60
"""
mark = int(input("Enter your marks : "))
if mark < 0 or mark > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif mark >= 90:
  print("A")
elif mark >=80:
  print("B")
elif mark >=70:
  print("C")
elif mark >=60:
  print("D")
else :
  print("F")

 