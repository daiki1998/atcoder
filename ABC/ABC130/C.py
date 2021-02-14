
W, H, x, y = map(int, input().split())

res = W*H/2
if x == W/2 and y == H/2:
    print(res, 1)
else:
    print(res, 0)