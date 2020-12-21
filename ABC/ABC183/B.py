Sx, Sy, Gx, Gy = map(int, input().split())

res = Sx + (Gx-Sx) * Sy / (Sy + Gy)

print(res)