
N = int(input())
H = list(map(int, input().split()))

max_h = H[0]
res = 1
for i in range(1, N):
    if max_h <= H[i]:
        res += 1
    max_h = max(max_h, H[i])
print(res)
