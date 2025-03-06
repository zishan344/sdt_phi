n = int(input())
arr = list(map(int,input().split()))
MinVal = min(arr)
MaxVal = max(arr)

for i in range(n):
  if(arr[i] == MinVal):
    arr[i] = MaxVal
  elif(arr[i] == MaxVal):
    arr[i] = MinVal

for i in arr:
  print(i,end=' ')