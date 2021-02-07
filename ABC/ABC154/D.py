N, K = map(int, input().split())
P = list(map(int, input().split()))

X = []
for i in range(N):
    X.append((P[i]*10**6+10**6)/2)

res_list = [0 for i in range(N)]
res_list[0] = X[0]
for i in range(1, N):
    res_list[i] = X[i] + res_list[i-1]
    if i >= K:
        res_list[i] -= X[i-K]

print(max(res_list)/10**6)