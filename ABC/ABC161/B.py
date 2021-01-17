
N, M = map(int, input().split())
A = list(map(int, input().split()))

res = 0
sum_A = sum(A)
h = sum_A / (4*M)
for i in range(N):
    if h <= A[i]:
        res += 1

if res >= M:
    print("Yes")
else:
    print("No")