
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
d = list(reversed(divisor(N)))
res = 0
for i in range(len(d)):
    nokori = N - d[i]
    ato = nokori/d[i]
    if ato%2 == 0:
        res += 2
print(res)