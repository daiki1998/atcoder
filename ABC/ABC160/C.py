
K, N = map(int, input().split())

A = list(map(int, input().split()))

A.append(K+A[0])
B = []
for i in range(1, len(A)):
    B.append(A[i]-A[i-1])
max_b = max(B)
print(K-max_b)
