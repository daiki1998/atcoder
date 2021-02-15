
S = input()
zero_cnt = 0
one_cnt = 0
for i in range(len(S)):
    if S[i] == "0":
        zero_cnt += 1
    else:
        one_cnt += 1
print(min(zero_cnt, one_cnt)*2)