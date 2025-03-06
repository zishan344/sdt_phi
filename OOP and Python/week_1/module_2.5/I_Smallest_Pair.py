import sys
t = int(input())
for k in range(t):
  n =int(input())
  arr=list(map(int,input().split()))
  
  minVal= sys.maxsize
  for i in range(0, n):
     for j in range(i+1, n):
        val = arr[i] + arr[j] + j - i
        minVal = min(val,minVal)
  print(minVal)
         
     
  