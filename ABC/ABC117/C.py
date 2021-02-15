
N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
res = []
for i in range(M-1):
    res.append(X[i+1]-X[i])
res.sort(reverse=True)
print(sum(res[N-1:]))