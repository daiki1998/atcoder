

N, M = map(int, input().split())
X_Y = []
for _ in range(M):
    X_Y.append(tuple(map(int, input().split())))

res = 1
for i in range(2**N):
    cnt = 0
    S = []
    for j in range(N):
        if ((i >> j) & 1):
            if S == []:
                S.append(j+1)
                cnt += 1
            else:
                for s in S:
                    x, y = min(j+1, s), max(j+1, s)
                    if (x, y) in X_Y:
                        pass
                    else:
                        cnt -= 100
                if cnt > 0:
                    cnt += 1
                    S.append(j+1)

    res = max(res, cnt)
print(res)