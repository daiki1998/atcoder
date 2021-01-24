
N, X = map(int, input().split())

L = []
cnt = 0
for _ in range(N):
    v, p = map(int, input().split())
    L.append(v*p)
X = X*100
res = -1
for i in range(1, N+1):
    cnt += L[i-1]
    if cnt > X:
        res = i
        break
print(res)

