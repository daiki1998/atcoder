
H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

h_index = []
for h in range(H):
    h_set = set(a[h])
    if "#" in h_set:
        h_index.append(h)
a_ch = []
for h in h_index:
    a_ch.append(a[h])
a_ch = list(zip(*a_ch))
a_ch = [list(x) for x in a_ch]
h_index = []
for h in range(len(a_ch)):
    h_set = set(a_ch[h])
    if "#" in h_set:
        h_index.append(h)
a_ch_ch = []
for h in h_index:
    a_ch_ch.append(a_ch[h])
a_ch_ch = list(zip(*a_ch_ch))
a_ch_ch = [list(x) for x in a_ch_ch]
for i in range(len(a_ch_ch)):
    for j in range(len(a_ch_ch[i])):
        print(a_ch_ch[i][j], end="")
    print()
