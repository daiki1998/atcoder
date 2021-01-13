import operator

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
X_Y = [[0, 0]]
for i in range(M):
    x, y = map(int, input().split())
    X_Y.append([x, y])

X_Y = sorted(X_Y, key=operator.itemgetter(0, 1), reverse=True)

dp = [-10**9-1 for i in range(N+1)]

for i in range(M):
    dp[X_Y[i][0]] = max(A[X_Y[i][1]] - A[X_Y[i][0]], dp[X_Y[i][0]], A[X_Y[i][1]] - A[X_Y[i][0]] + dp[X_Y[i][1]])
print(max(dp))