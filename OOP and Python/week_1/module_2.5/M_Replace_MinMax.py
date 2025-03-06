n = int(input())
arr=list(map(int,input().split()))
mini = min(arr)
maxi = max(arr)
for i in range(0,len(arr),1):
  if arr[i] == mini:
   arr[i] = maxi
  elif arr[i] == maxi:
    arr[i] = mini
for i in arr:
  print(i,end=" ")
  