import math

N = int(input())

ans = []
s_N = int(math.sqrt(N))

for i in range(1, s_N+1):
    if N % i == 0:
        ans.append(i)
        ans.append(N//i)

ans = list(set(ans))
ans.sort()
for a in ans:
    print(a)
