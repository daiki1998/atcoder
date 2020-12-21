A = list(map(int, input().split()))

d = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
def f(x, y, z, d):
    if d[x][y][z] != 0:
        return d[x][y][z]
    elif x == 100 or y == 100 or z == 100:
        return 0
    else:
        d[x][y][z] = x/(x+y+z)*(f(x+1,y,z, d)+1) + y/(x+y+z)*(f(x,y+1,z, d)+1)+z/(x+y+z)*(f(x,y,z+1, d)+1)
        return d[x][y][z]

print(f(A[0], A[1], A[2], d))