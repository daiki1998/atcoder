from collections import defaultdict
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
N = int(input())
N_d = divisor(N)[1:]
done_n = []
res = 0
for n in N_d:
    if n > N:
        break
    n_d = divisor(n)
    if (len(n_d) == 2 or n in done_n) and N % n == 0:
        N //= n
        res += 1
        done_n.append(n*n_d[1])
print(res)
