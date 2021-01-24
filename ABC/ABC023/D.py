
N = int(input())
H, S, M = [], [], 0
for _ in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)
    M = max(h+s*N, M)

l, r = max(H), M
m = (r+l) // 2
while r-l > 1:
    dp = []
    flag = True
    for i in range(N):
        dp.append((m - H[i])//S[i])
    dp.sort()
    for i in range(N):
        if i > dp[i]:
            flag = False
            break
    if flag:
        r = m
        m = (m+l)//2
    else:
        l = m
        m = (m+r)//2


dp = []
flag = True
for i in range(N):
    dp.append((m - H[i])//S[i])
dp.sort()
for i in range(N):
    if i > dp[i]:
        flag = False
        break
if flag:
    print(m)
else:
    print(m+1)