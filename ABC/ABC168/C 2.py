import math
A, B, H, M = map(int, input().split())

A_kakudo = 360 * H / 12 + (360 / 12) * M / 60
B_kakudo = 360 * M / 60

if A_kakudo >= B_kakudo:
    kakudo = A_kakudo - B_kakudo
else:
    kakudo = B_kakudo - A_kakudo
res = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(kakudo)))

print(res)