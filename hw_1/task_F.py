l1, w1, l2, w2 = map(int, input().split())

res1 = (w1 + w2) * max(l1, l2)
res2 = (w1 + l2) * max(l1, w2)
res3 = (l1 + l2) * max(w1, w2)
res4 = (l1 + w2) * max(w1, l2)

final = min(res1, res2, res3, res4)

if res1 == final:
    print(w1 + w2, max(l1, l2))
elif res2 == final:
    print(w1 + l2, max(l1, w2))
elif res3 == final:
    print(l1 + l2, max(w1, w2))
else:
    print(l1 + w2, max(w1, l2))
