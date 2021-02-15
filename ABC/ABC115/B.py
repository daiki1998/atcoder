
N = int(input())
p = [int(input()) for _ in range(N)]

p.sort()
print(sum(p)-p[-1]//2)