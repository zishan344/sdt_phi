n,t =  input().split(' ')
n = int(n)
t = int(t)
arr=list(map(int,input().split()))

prefixSum =[]
prefixSum.append(arr[0])

for i in range(1,n):
  prefixSum.append(arr[i]+prefixSum[i-1])


for i in range(t):
  l,r =  input().split(' ')
  l = int(l)
  r = int(r)
  if l-2 >= 0:
    val = prefixSum[r-1]-prefixSum[l-2]
    print(val)
  elif l-2 < 0:
    print(prefixSum[r-1])