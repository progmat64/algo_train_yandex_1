a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0 and b == c * c:
    print("MANY SOLUTIONS")
else:
    if a != 0:
        x = c * c - b
        if x / a == x // a:
            print(x // a)
    else:
        print("NO SOLUTION")
