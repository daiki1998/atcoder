
N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(N):
    if A[i] == res+1:
        res += 1
if res == 0:
    print(-1)
else:
    print(N-res)