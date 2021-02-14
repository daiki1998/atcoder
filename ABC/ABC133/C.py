
L, R = map(int, input().split())
mod = 2019

L_mod = L % mod
if L+(mod-L_mod) <= R:
    res = 0
else:
    res = 2020
    for i in range(L, R):
        for j in range(i+1, R+1):
            res = min(res, ((i % mod) * (j % mod)) % mod)
print(res)