N, A, B = map(int, input().split())

res = 0
for i in range(N+1):
    if A <= sum(list(map(int, list(str(i))))) <= B:
        res += i
print(res)