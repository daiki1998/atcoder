
H = int(input())
cnt = 1
res = 0
while H > 0:
    res += cnt
    cnt *= 2
    H //= 2
print(res)