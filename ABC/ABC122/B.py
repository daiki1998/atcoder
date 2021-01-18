
S = input()

l = ["A", "C", "G", "T"]
res = 0
s = [0]
for i in range(len(S)):
    if S[i] in l:
        s.append(1)
    else:
        s.append(0)
for i in range(1, len(s)):
    if s[i] == 0:
        s[i] = 0
    else:
        s[i] = s[i-1] + s[i]
print(max(s))

