# print 1 to n
n = 10
for i in range(0, n+1, 1):
  print(i,end="")

# print odd numbers
num = 10
for i in range(num):
  if i % 2 != 0:
    print(i,end=",")

# print array avg

avgArr=list(map(int,input("Enter a numbers: ").split()))
sz = len(avgArr)
print(avgArr)
sum = 0
for i in avgArr:
   sum +=i
 
avg = sum/sz
print(sum)  

# print max and minimum value in array

maxMinArr =list(map(int, input("enter the elements").split()))
print(max(maxMinArr))
print(min(maxMinArr))


# print the number in array which divided by integers
divArr = list(map(int, input("enter the elements: ").split()))
for num in divArr: 
   if  num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
     print(num)
