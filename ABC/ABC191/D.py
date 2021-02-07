import math
from decimal import Decimal

X, Y, R = map(Decimal, input().split())

bottom = math.ceil(X-R)
top = math.floor(X+R)
res = 0
for i in range(bottom, top+1):
    b = i-X
    p = (R**2 - b**2).sqrt()
    right = math.floor(Y + p)
    left = math.ceil(Y - p)
    res += int(right - left) + 1
print(res)