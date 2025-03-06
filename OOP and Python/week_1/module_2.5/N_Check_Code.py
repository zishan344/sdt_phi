a, b = map(int, input().split())
s = input()

if len(s) != a + b + 1:
    print("No")
else:
    if s[a] == '-':        
        s1, s2 = s[:a], s[a+1:]
        if s1.isdigit() and s2.isdigit():
            print("Yes")
        else:
            print("No")
    else:
        print("No")