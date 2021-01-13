
N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

res = 0
for i in range(N):
    for j in range(i+1, N):
        k = (Y[j]-Y[i]) / (X[j] - X[i])
        if -1 <= k <= 1:
            res += 1
print(res)