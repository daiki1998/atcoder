
N, K = map(int, input().split())

a = N % K
print(min(a, abs(K-a)))