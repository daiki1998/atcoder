
N = int(input())
num = set([i*j for i in range(1, 10) for j in range(1, 10)])

if N in num:
    print("Yes")
else:
    print("No")