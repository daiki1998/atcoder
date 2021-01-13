K = int(input())

res = -1
A = [-1, 7%K]
for i in range(1, K):
    A.append((A[-1]*10+7)%K)
for i in range(K+1):
    if A[i] == 0:
        res = i
        break
print(res)