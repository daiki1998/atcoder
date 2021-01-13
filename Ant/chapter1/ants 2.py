L = int(input())
n = int(input())
X = list(map(int, input().split()))

min_list = [min(x, L-x) for x in X]
min_num = max(min_list)
max_list = [max(x, L-x) for x in X]
max_num = max(max_list)

print(min_num, max_num)