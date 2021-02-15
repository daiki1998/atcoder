
N, T = map(int, input().split())

min_c = 1001
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        min_c = min(min_c, c)
if min_c == 1001:
    print("TLE")
else:
    print(min_c)