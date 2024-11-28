divArr = list(map(int, input("enter the elements: ").split()))
for num in divArr: 
   if  num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
     print(num)