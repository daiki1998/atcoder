N = int(input())
A = list(map(int, input().split()))

res = 0
max_num = A[0]
for i in range(1, N):
    max_num = max(max_num, A[i])
    res += max(0, max_num-A[i])
print(res)