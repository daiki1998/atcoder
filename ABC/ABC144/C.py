
N = int(input())

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

l = divisor(N)
res = N
for i in range(len(l)):
    a, b = l[i], N//l[i]
    res = min(a+b-2, res)
print(res)