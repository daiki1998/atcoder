
N, K = map(int, input().split())
H = list(map(int, input().split()))

res = 0
for i in range(N):
    if H[i] >= K:
        res += 1
print(res)