
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

Z_x = max(x)
Z_y = min(y)

if X < Z_x < Z_y <= Y:
    print("No War")
else:
    print("War")