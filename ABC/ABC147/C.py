
from collections import defaultdict

N = int(input())
A = []
X_Y = []
for _ in range(N):
    A.append(int(input()))
    x_y = []
    for _ in range(A[-1]):
        x_y.append(list(map(int, input().split())))
    X_Y.append(x_y)

res = 0
for i in range(2**N):
    flag = True
    cnt = 0
    d = defaultdict(int)
    for j in range(N):
        if (i >> j) & 1:
            cnt += 1
            if d[j+1] == 0:
                d[j+1] = 2
            else:
                if d[j+1] == 1:
                    flag = False
            for k in range(A[j]):
                if d[X_Y[j][k][0]] == 0:
                    d[X_Y[j][k][0]] = X_Y[j][k][1] + 1
                elif d[X_Y[j][k][0]] == 1:
                    if X_Y[j][k][1] != 0:
                        flag = False
                else:
                    if X_Y[j][k][1] != 1:
                        flag = False
        else:
            if d[j + 1] == 0:
                d[j + 1] = 1
            else:
                if d[j + 1] == 2:
                    flag = False
    if flag:
        res = max(res, cnt)
print(res)