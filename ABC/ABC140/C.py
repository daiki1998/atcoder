
N = int(input())
B = list(map(int, input().split()))

res = 0
for i in range(N):
    if i == 0:
        res += B[i]
    elif i == N-1:
        res += B[i-1]
    else:
        res += min(B[i-1], B[i])
print(res)