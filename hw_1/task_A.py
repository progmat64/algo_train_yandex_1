tr, tc = map(int, input().split())
s = input()

if s == "freeze":
    if tr > tc:
        print(tc)
    else:
        print(tr)
if s == "heat":
    if tr < tc:
        print(tc)
    else:
        print(tr)
if s == "auto":
    print(tc)
if s == "fan":
    print(tr)
