
H, N = map(int, input().split())
A = list(map(int, input().split()))

sum_num = sum(A)
if sum_num >= H:
    print("Yes")
else:
    print("No")