
N = int(input())
P = list(map(int, input().split()))

min_num = P[0]
res = 1
for i in range(1, N):
    if P[i] <= min_num:
        res += 1
    min_num = min(P[i], min_num)
print(res)