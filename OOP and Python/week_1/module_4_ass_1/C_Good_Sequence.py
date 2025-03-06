n = int(input())
arr = list(map(int, input().split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
cnt = 0
for k,v in freq.items():
  if k > v:
    cnt += v
  elif k < v:
    cnt += (v - k)
print(cnt)