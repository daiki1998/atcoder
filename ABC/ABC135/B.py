
N = int(input())

p = list(map(int, input().split()))

p_sort = sorted(p)
cnt = 0
for i in range(N):
    if p[i] != p_sort[i]:
        cnt += 1
if cnt < 3:
    print("YES")
else:
    print("NO")