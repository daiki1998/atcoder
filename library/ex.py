M = int(input())
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def dfs(n, m, cnt, visit):
    global res
    now_pos = [n, m]
    visit[n][m] = True
    now_cnt = cnt
    for action in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        next_pos = [now_pos[0]+action[0], now_pos[1]+action[1]]
        if 0 <= next_pos[0] < N and 0 <= next_pos[1] < M and A[next_pos[0]][next_pos[1]] == 1 and visit[next_pos[0]][next_pos[1]] == False:
            now_cnt += 1
            dfs(next_pos[0], next_pos[1], now_cnt, visit)
            now_cnt = cnt
        else:
            res = max(now_cnt, res)
    visit[n][m] = False

res = 0
for n in range(N):
    for m in range(M):
        if A[n][m] == 1:
            cnt, visit = 1, [[False for _ in range(M)] for _ in range(N)]
            dfs(n, m, cnt, visit)
print(res)