n = int(input())
l = [int(x) for x in input().split()]

max_l = max(l)
sum_l = sum(l) - max_l

if max_l < sum_l:
    print("Yes")
else:
    print("No")