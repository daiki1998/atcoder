X, Y = map(int, input().split())

if X > Y:
    X, Y = Y, X

res_1 = Y // X - (Y // X) % 2
res_2 = Y - X * res_1
# res_3 =

print(res_1)
print(res_2)

