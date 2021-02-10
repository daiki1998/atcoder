from itertools import combinations

N = int(input())
D = list(map(int, input().split()))

res = 0
for com in combinations(range(N), 2):
    res += D[com[0]]*D[com[1]]
print(res)
