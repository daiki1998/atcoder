from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

res = 0
k = K
i = 0
while k > 0:
    h = min(k, d[i])
    n = k - h
    res += i * n
    k = k - n
    i += 1

print(res)
