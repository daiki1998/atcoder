
N = int(input())
S = input()
index = ord("A")
res = ""
for i in range(len(S)):
    next = (ord(S[i]) - ord("A") + N) % (ord("Z") - ord("A") + 1) + ord("A")
    res += chr(next)
print(res)