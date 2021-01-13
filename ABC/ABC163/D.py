
N, K = map(int, input().split())

res = 0
mod = 10**9+7


for i in range(K, N+2):
    res += (i*(N-i+1)+ 1)
    res %= mod

if K > N:
    res = 1
print(res)