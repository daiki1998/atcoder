
N = int(input())
d = list(map(int, input().split()))

d.sort()
res = d[N//2] - d[N//2-1]
print(res)