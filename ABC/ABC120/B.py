# 約数をリストで返す
def divisor(N):
    i = 1
    l = []
    while i**2 <= N:
        if N % i == 0:
            l.append(i)
            if i**2 != N:
                l.append(N//i)
        i += 1
    return (sorted(l))

A, B, K = map(int, input().split())

div_A = divisor(A)
div_B = divisor(B)
div = sorted(list(set(div_A) & set(div_B)))
print(div[-K])
