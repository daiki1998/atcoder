n = int(input())
A = list(map(int, input().split()))
A.sort()
res = 0
for i in range(n):
    if i <= n-3:
        for j in range(i+1, n):
            if j <= n-2:
                for k in range(j+1,n):
                    length = A[i]+A[j]+A[k]
                    if A[i]+A[j] > A[k]:
                        res = max(res, length)
print(res)
