a = int(input())
b = int(input())
n = int(input())
m = int(input())

min1 = a * (n - 1) + n
max1 = a * (n + 1) + n
min2 = b * (m - 1) + m
max2 = b * (m + 1) + m

min_answer = max(min1, min2)
max_answer = min(max1, max2)

if min_answer > max_answer:
    print(-1)
else:
    print(min_answer, max_answer)
