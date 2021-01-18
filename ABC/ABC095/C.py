
A, B, C, X, Y = map(int, input().split())

res = 10**11
max_X_Y = max(X, Y)
for c in range(0, (max_X_Y+1)*2, 2):
    res = min(res, A*(max(X-c//2, 0))+B*(max(Y-c//2, 0))+C*c)
print(res)