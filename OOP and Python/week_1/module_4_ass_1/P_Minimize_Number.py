import sys
n = int(input())
numbers = list(map(int, input().split()))

mNum = sys.maxsize
#print(mNum)
for i in numbers:
  if i % 2 != 0:
    mNum = 0
    break
  else:
    cnt = 0
    while i % 2 == 0:
      i = i/2
      cnt+=1
    mNum = min(mNum, cnt)
print(mNum)