
N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)
res = sum(H[K:])
print(res)
