N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = [A[0]]
for i in range(1, N):
    B.append(B[i-1] + A[i])
A.sort()
B.sort(reverse=True)
res = 0
for i in range(N-1):
    res += A[i]*B[i+1]
print(res % (10**9 + 7))