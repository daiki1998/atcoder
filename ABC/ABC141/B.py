
S = input()

res = "Yes"
for i in range(1, len(S)+1):
    if i % 2 == 1:
        if S[i-1] == "L":
            res = "No"
    else:
        if S[i-1] == "R":
            res = "No"
print(res)