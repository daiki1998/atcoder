
N = int(input())
W = [input() for _ in range(N)]

word_set = set()
word_set.add(W[0])
back = W[0][-1]
res = "Yes"
for i in range(1, N):
    if W[i] in word_set or back != W[i][0]:
        res = "No"
    word_set.add(W[i])
    back = W[i][-1]
print(res)
