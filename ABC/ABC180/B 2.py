import math

N = int(input())
X = list(map(int, input().split()))

m, u, c = 0, 0, []

for i in range(N):
    m += abs(X[i])
    u += X[i]**2
    c.append(abs(X[i]))

print(m)
print(math.sqrt(u))
print(max(c))
