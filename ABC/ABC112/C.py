
N = int(input())
X, Y, H = [], [], []
for _ in range(N):
    x, y, h = map(int, input().split())
    X.append(x)
    Y.append(y)
    H.append(h)

H_one = [i for i in range(N) if H[i] > 0]
if len(H_one) == 1:
    res = [X[H_one[0]], Y[H_one[0]], H[H_one[0]]]
else:
    for cx in range(101):
        for cy in range(101):
            real_H = []
            for i in range(N):
                if H[i] == 0:
                    continue
                real_H.append(H[i] + abs(X[i]-cx) + abs(Y[i]-cy))
            if len(set(real_H)) == 1 and 0 < real_H[0]:
                res = [cx, cy, real_H[0]]
print("{} {} {}".format(res[0], res[1], res[2]))