
N = int(input())
A = list(map(int, input().split()))

A.sort()
res = 0

for i in range(N):
    res = res + A[i]*i - A[i] *(N-1-i)

print(res)