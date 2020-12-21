N = int(input())
T, X, Y = [0], [0], [0]

for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

res = "Yes"
for i in range(1, N+1):
    time = T[i] - T[i-1]
    x = X[i] - X[i-1]
    y = Y[i] - Y[i-1]
    sum_dis = abs(x) + abs(y)
    idoT = time - sum_dis
    if idoT < 0 or idoT % 2 == 1:
        res = "No"
print(res)