
A, B = map(int, input().split())

k = abs(B+A)
if k % 2 == 0:
    print(int(k//2))
else:
    print("IMPOSSIBLE")
