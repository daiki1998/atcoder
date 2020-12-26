from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A.sort()
max_A = max(A)
dp = [True for _ in range(max_A+1)]
cont = Counter(A)
res = 0
for i in range(N):
    if dp[A[i]] == True and cont[A[i]] == 1:
        res += 1
    if dp[A[i]] == True:
        num = A[i]
        while num < max_A+1:
            dp[num] = False
            num += A[i]

print(res)
