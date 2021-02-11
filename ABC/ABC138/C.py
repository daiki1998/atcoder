
N = int(input())
V = list(map(int, input().split()))

res = 0
for i in range(N-1):
    V.sort()
    item = [V[0], V[1]]
    del V[0]
    del V[0]
    V.append(sum(item)/2)
print(V[0])
