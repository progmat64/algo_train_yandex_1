a = int(input())
b = int(input())
c = int(input())

if (a > (b + c)) or (b > (a + c)) or (c > (b + a)):
    print("NO")
else:
    print("YES")
