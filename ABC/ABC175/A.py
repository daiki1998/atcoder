S = input()

count = 0
c = 0
for s in S:
    if s == "S":
        c = 0
    else:
        c += 1
    count = max(c, count)

print(count)