N = int(input())
A = list(map(int, input().split()))

res = 1
if 0 in A:
    res = 0
else:
    for i in range(N):
        res *= A[i]
        if res > 10**18:
            res = -1
            break
print(res)