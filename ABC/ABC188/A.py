X, Y = map(int, input().split())

res = abs(X-Y)

if res >= 3:
    print("No")
else:
    print("Yes")