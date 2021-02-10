
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
res = 0

pre = N+1
for i in range(N):
    res += B[A[i]-1]
    if A[i] == pre:
        res += C[pre-2]
    pre = A[i]+1
print(res)