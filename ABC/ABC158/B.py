
N, A, B = map(int, input().split())

res, amari = N // (A+B), N % (A+B)
print(res*A + min(amari, A))