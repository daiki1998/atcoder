import itertools

N, K = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))

nums = list(range(1, N))
ans = 0
for index in itertools.permutations(nums):
    index = [0]+list(index)
    ti = 0
    for i in range(N):
        ti += T[index[i]][index[(i+1)%N]]
    if ti == K:
        ans += 1

print(ans)