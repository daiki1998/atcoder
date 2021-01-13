from functools import reduce
import math
# 最大公約数
def gcd(l):
    """
    :param l: 最大公約数を求めたいリスト
    :return: 最大公約数
    """
    return reduce(math.gcd, l)

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

T = int(input())
N, S, K = [], [], []
for i in range(T):
    n, s, k = map(int, input().split())
    N.append(n)
    S.append(s)
    K.append(k)

for t in range(T):
    g = gcd([N[t], S[t], K[t]])
    print(g)
    N[t], S[t], K[t] = int(N[t]/g), int(S[t]/g), int(K[t]/g)
    if gcd([N[t], K[t]]) != 1:
        print(-1)
    else:
        print((-S[t]*pow(K[t], -1, N[t]))%N[t])

