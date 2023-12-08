a = int(input())
b = int(input())
n = int(input())
m = int(input())

train_1_min_time = 0
train_1_max_time = 0

train_2_min_time = 0
train_2_max_time = 0

for i in range(n):
    if i == 0:
        train_1_max_time += a
    if i == (n - 1):
        train_1_min_time -= 1
    train_1_max_time += a + 1
    train_1_min_time += a + 1

for j in range(m):
    if j == 0:
        train_2_max_time += b
    if j == (m - 1):
        train_2_min_time -= 1
    train_2_max_time += b + 1
    train_2_min_time += b + 1

train_1_min_time += 1 - a
train_2_min_time += 1 - b

if max(train_1_min_time, train_2_min_time) > min(
    train_1_max_time, train_2_max_time
):
    print(-1)

else:
    print(
        max(train_1_min_time, train_2_min_time),
        min(train_1_max_time, train_2_max_time),
    )
