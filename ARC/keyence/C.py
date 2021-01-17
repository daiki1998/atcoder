
H, W, K = map(int, input().split())

mas = [["" for _ in range(H)] for _ in range(W)]

for _ in range(K):
    h, w, c = input().split()
    mas[int(h)-1][int(w)-1] = c

print(mas)

dp = [[None for _ in range(H)] for _ in range(W)]
