
from collections import defaultdict
n = int(input())
v = list(map(int, input().split()))

if len(set(v)) == 1:
    print(n//2)
else:
    odd = defaultdict(int)
    even = defaultdict(int)
    for i in range(1, n+1):
        if i % 2 == 0:
            even[v[i-1]] += 1
        else:
            odd[v[i-1]] += 1
    odd_max_index = [0, 0]
    odd_list = []
    for k, val in odd.items():
        odd_list.append(val)
        if odd_max_index[0] < val:
            odd_max_index = [val, k]
    odd_list.sort(reverse=True)
    even_max_index = [0, 0]
    even_list = []
    for k, val in even.items():
        even_list.append(val)
        if even_max_index[0] < val:
            even_max_index = [val, k]
    even_list.sort(reverse=True)
    if even_max_index[1] == odd_max_index[1]:
        if even_list[0]+odd_list[1] >= even_list[1] + odd_list[0]:
            res = n - (even_list[0] + odd_list[1])
        else:
            res = n - (odd_list[0] + even_list[1])
    else:
        res = n - (odd_list[0]+even_list[0])
    print(res)