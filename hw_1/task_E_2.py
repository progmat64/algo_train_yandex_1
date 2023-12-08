K1, M, K2, P2, N2 = map(int, input().split())

total_floor = M * (P2 - 1) + N2

apartments_on_floor = round(K2 / total_floor)

total_apartments_in_entrance = apartments_on_floor * M


if total_apartments_in_entrance * (P2 - 1) >= K2:
    print(-1, -1)
    exit()

if N2 == 1:
    if M == 1:
        print(0, 1)
        exit()
    if M > 1:
        print(0, 0)
        exit()

P1 = 1
helping = total_apartments_in_entrance

while K1 > helping:
    P1 = P1 + 1
    helping *= 2


max_padik = total_apartments_in_entrance * P1


N2 = M + 1
while K1 < max_padik:
    N2 = N2 - 1
    max_padik = max_padik - apartments_on_floor

N1 = N2

print(P1, N1)
