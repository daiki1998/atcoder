N = int(input())
D = []
for _ in range(N):
    D.append(int(input()))

D.sort()
count = 1
for i in range(1, N):
    if D[i-1] != D[i]:
        count += 1

"""
count = len(set(D))
"""
print(count)

