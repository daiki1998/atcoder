
N = int(input())
P = []
X = 0
for _ in range(N):
    a, b = map(int, input().split())
    P.append(2*a+b)
    X -= a

P.sort(reverse=True)
res = 0

for i in range(N):
    X += P[i]
    res += 1
    if X > 0:
        break
print(res)