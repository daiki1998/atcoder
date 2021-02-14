import math

N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
res = 0
for i in range(N):
    for j in range(i+1, N):
        l = 0
        for d in range(D):
            l += (X[i][d] - X[j][d])**2
        l = math.sqrt(l)
        if int(l) == l:
            res += 1
print(res)