N = str(input())
res = 0
for i in range(len(N)):
    res += int(N[i])
if res % 9 == 0:
    print("Yes")
else:
    print("No")

