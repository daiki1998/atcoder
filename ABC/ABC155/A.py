
A = list(map(int, input().split()))

if len(set(A)) == 1 or len(set(A)) == 3:
    print("No")
else:
    print("Yes")
