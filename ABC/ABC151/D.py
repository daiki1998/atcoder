
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))


res = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            start = [i, j]
            max_res = 0
            node = [start]
            dp = [[1000 for _ in range(W)] for _ in range(H)]
            dp[i][j] = 0
            while True:
                if node == []:
                    break
                now_pos = node[0]
                del node[0]
                for action in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    next_node = [now_pos[0]+action[0], now_pos[1]+action[1]]
                    if 0 <= next_node[0] < H and 0 <= next_node[1] < W and S[next_node[0]][next_node[1]] == ".":
                        if dp[next_node[0]][next_node[1]] > dp[now_pos[0]][now_pos[1]] + 1:
                            node.append(next_node)
                            dp[next_node[0]][next_node[1]] = dp[now_pos[0]][now_pos[1]] + 1
                            max_res = max(max_res, dp[next_node[0]][next_node[1]])
            res = max(res, max_res)
print(res)