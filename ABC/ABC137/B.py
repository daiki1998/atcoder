
K, X = map(int, input().split())

res = [i for i in range(X-K+1, X+K)]

for i in range(len(res)):
    print(res[i], end=" ")
print()