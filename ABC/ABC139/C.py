
N = int(input())
H = list(map(int, input().split()))

res = 0
cnt = 0
now = H[0]
for i in range(1, N):
    if H[i] <= now:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 0
    now = H[i]
res = max(res, cnt)

print(res)