Str = input().split('EGYPT')

newStr =""
for i in range(len(Str)):
  val = Str[i]
  if i < len(Str) - 1:
    newStr += f"{val} "
  else:
    newStr += val
print(newStr)