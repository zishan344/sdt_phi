n = int(input())
dp=[-1 for i in range(51)]

def fib(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  if dp[n]!=-1:
    return dp[n] 
  dp[n] = fib(n-1) + fib(n-2)
  return dp[n]

print(fib(n)) 