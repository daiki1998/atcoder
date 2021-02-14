
N, M = map(int, input().split())

l = [0 for _ in range(0, N+2)]

for _ in range(M):
    L, R = map(int, input().split())
    l[L] += 1
    l[R+1] -= 1
for i in range(1, N+2):
    l[i] += l[i-1]
res = 0
for i in range(N+2):
    if l[i] == M:
        res += 1
print(res)