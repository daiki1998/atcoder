A, B, C, K = map(int, input().split())

res = 0

if A >= K:
    print(K)
elif A+B >= K:
    print(A)
else:
    print(A + (-1) * (K - (A+B)))
