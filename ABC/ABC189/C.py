
N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(N):
    min_cnt = A[i]
    for j in range(i, N):
        min_cnt = min(min_cnt, A[j])
        res = max(res, min_cnt*(j-i+1))

print(res)
