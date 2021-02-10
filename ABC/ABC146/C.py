
A, B, X = map(int, input().split())

l, r = 1, 10**9

while r - l > 1:
    mid = (l+r)//2
    cnt = A * mid + B * len(str(mid))
    if cnt == X:
        break
    elif cnt > X:
        r = mid
    else:
        l = mid
if mid == 2:
    res = 0
    for i in range(1, 4):
        if X >= A * i + B * len(str(i)):
            res = i
else:
    for i in range(mid-2, mid+3):
        if X >= A * i + B * len(str(i)) and i <= 10**9:
            res = i
print(res)