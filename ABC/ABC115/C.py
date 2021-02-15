
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()
res = []
for i in range(N-K+1):
    res.append(h[i+K-1]-h[i])
print(min(res))