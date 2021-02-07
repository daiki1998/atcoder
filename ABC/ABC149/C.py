from collections import defaultdict
import bisect

X = int(input())

d = defaultdict(bool)
prime_list = []
for i in range(2, 10**5+4):
    if d[i] == False:
        prime_list.append(i)
        d[i] = True
        if i <= (10**5+4)**0.5:
            for j in range(i, 10**5+4, i):
                d[j] = True

index = bisect.bisect_left(prime_list, X)

print(prime_list[index])