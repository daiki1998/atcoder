def num_C_num(n_1, n_2, mod):
    X, Y = 1, 1
    for i in range(n_2):
        Y *= (i+1)
        Y %= mod
        X *= (n_1-i)
        X %= mod
    return (X * (pow(Y, mod-2, mod))) % mod

n, a, b = map(int, input().split())
mod = 10**9+7
d = pow(2, n, mod)-1
fa = num_C_num(n, a, mod) % mod
fb = num_C_num(n, b, mod) % mod
res = (d - fa - fb) % mod
print(res)