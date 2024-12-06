Str = input().split(' ')
newStr = ""
for i in range(len(Str)):
    val = Str[i]
    newStr += val[::-1]
    if i < len(Str) - 1:
        newStr += " "

print(newStr)