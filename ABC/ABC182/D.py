N = int(input())
A = list(map(int, input().split()))

A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[-1]+A[i])
pos = 0
A_max = [0]
res = 0
for i in range(1, N+1):
    A_max.append(max(A_max[-1], A_sum[i]))
    res = max(res, A_max[i]+pos)
    pos += A_sum[i]

print(res)