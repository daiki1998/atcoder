from collections import defaultdict

def dfs(i, l, s, res):
    if l != []:
        print(l, res)
        now_num = l[-1]
        del l[-1]
        if now_num not in s:
            s.add(now_num)
            l += d[now_num]
            res[now_num].append(i)
            i += 1
            index = dfs(i, l, s, res)
            res[now_num].append(index)
            i += 1
            return i
        else:
            return i
    else:
        return i

U = int(input())
d = defaultdict(list)
for _ in range(U):
    k_v = list(map(int, input().split()))
    if k_v[1] == 0:
        continue
    else:
        for e in k_v[2:]:
            d[k_v[0]].append(e)

print(d)
l = [1]
s = set()
i = 1
res = defaultdict(list)
dfs(i, l, s, res)
print(res)
