N, K = map(int, input().split())
section = []

for _ in range(K):
    l, r = map(int, input().split())
    section += [i for i in range(l, r+1)]

print(section)