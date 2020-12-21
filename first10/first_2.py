s = str(input())

res = 0

for i in range(len(s)):
    if s[i] == '1':
        res += 1
print(res)