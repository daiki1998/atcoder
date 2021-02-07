N, K, M = map(int,input().split())

A = list(map(int, input().split()))

res = M*N - sum(A)
if res <= K:
    print(max(0, res))
else:
    print(-1)