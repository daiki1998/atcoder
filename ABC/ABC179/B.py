N = int(input())
D = []
for _ in range(N):
    D.append(list(map(int, input().split())))

count = 0
res = "No"
for i in range(N):
    if D[i][0] == D[i][1]:
        count += 1
    else:
        count = 0
    if count == 3:
        res = "Yes"
        break
print(res)