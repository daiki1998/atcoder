from collections import defaultdict

N, X, Y = map(int, input().split())

res = [[0 for _ in range(N+1)] for _ in range(N+1)]
d = defaultdict(int)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if i <= X and Y <= j:
            d[j - i - (Y - X) + 1] += 1
            res[i][j] = j - i - (Y - X) + 1
        else:
            i_X = abs(X-i)
            j_Y = abs(Y-j)
            min_k = min(i_X+j_Y+1, j-i)
            d[min_k] += 1
            res[i][j] = min_k
for i in range(1, N):
    print(d[i])