N, K, M = map(int, input().split())

result = 0
realisation = N // K
remains = N % K

if N < K or K < M:
    print(0)
    raise SystemExit

for i in range(realisation):
    result += K // M
    remains += K % M

while remains >= K:
    realisation = remains // K
    remains = remains - realisation * K
    for i in range(realisation):
        result += K // M
        remains += K % M

print(result)
