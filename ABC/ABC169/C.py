A, B = map(float, input().split())

A = int(A)
B = float(B)
B_100 = B*100
B = round(B_100)
print(A*B//100)