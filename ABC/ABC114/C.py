
from itertools import combinations_with_replacement, permutations

N = int(input())

l = [3, 5, 7]
res = 0
s_set = set()
for i in range(3, len(str(N))+1):
    for comb in combinations_with_replacement(l, i):
        if len(set(comb)) != 3:
            continue
        for c in permutations(comb, len(comb)):
            now = 0
            for i in range(len(c)):
                now += c[i]*10**(i)
            if now <= N and now not in s_set:
                s_set.add(now)
                res += 1
print(res)