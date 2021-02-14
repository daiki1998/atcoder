
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0
for i in range(N):
    if B[i] >= A[i]:
        res += A[i]
        B[i] -= A[i]
        A[i] = 0
        if B[i] >= A[i+1]:
            res += A[i+1]
            B[i] -= A[i + 1]
            A[i+1] = 0
        else:
            res += B[i]
            A[i+1] -= B[i]
    else:
        res += B[i]
        A[i] -= B[i]
        B[i] = 0
print(res)