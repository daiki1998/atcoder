
A, B, T = map(int, input().split())

res = 0
for i in range(A, T+1, A):
    res += B
print(res)