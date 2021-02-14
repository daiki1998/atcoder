
N, L = map(int, input().split())

apple_list = [L+i-1 for i in range(1, N+1)]

res = 0
now = 1000
for i in range(N):
    res += apple_list[i]
    if abs(apple_list[i]) < abs(now):
        now = apple_list[i]
res -= now
print(res)