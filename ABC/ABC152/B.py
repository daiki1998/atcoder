
a, b = map(int, input().split())

A = str(a)*b
B = str(b)*a
A_B = [A, B]
A_B.sort()
print(A_B[0])