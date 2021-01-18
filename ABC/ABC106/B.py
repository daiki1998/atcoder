
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

N = int(input())

res = 0
for i in range(1, N+1):
    if len(divisor(i)) == 8 and i % 2 == 1:
        res += 1
print(res)
