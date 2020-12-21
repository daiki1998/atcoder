N = int(input())
count = 10 ** N - 9 ** N * 2 + 8 ** N
print(int(count % (10**9+7)))

