
N, X = map(int, input().split())

L = list(map(int, input().split()))

res = 1
now = 0
for i in range(N):
    now += L[i]
    if now <= X:
        res += 1
print(res)