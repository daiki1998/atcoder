
N, S, D = map(int, input().split())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

flag = False
for i in range(N):
    if X[i] < S and Y[i] > D:
        flag = True
if flag:
    print("Yes")
else:
    print("No")
