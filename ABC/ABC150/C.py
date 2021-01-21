from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

n_list = [i for i in range(1, N+1)]

p, q = 0, 0
for i, n in enumerate(list(permutations(n_list))):
    if list(n) == P:
        p = i+1
    if list(n) == Q:
        q = i+1
print(abs(p-q))