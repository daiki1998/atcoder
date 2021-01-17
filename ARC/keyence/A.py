
N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

c = [0]
a = 0
b = 0
for i in range(1, N+1):
    c.append(max(A[i]*B[i], A[i-1]*B[i], c[i-1]))
    print(c[-1])
    A[i] = max(A[i - 1], A[i])