N = int(input())
A = list(map(int, input().split()))

res = 0

for i in range(N):
    res += 1/A[i]
print(1/res)