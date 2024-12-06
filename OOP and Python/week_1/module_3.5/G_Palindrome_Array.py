n = int(input())
arr = list(map(int, input().split()))
arr2= arr[::-1]
flag = True

for i in range(n):
  if arr[i] != arr2[i]:
   flag = False
   break
if flag == True:
  print("YES")
else:
  print("NO")
   