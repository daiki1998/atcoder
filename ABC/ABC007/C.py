from collections import deque

H, W = map(int, input().split())
start = list(map(int, input().split()))
goal = list(map(int, input().split()))
C = [["#" for _ in range(W+1)]]
for _ in range(H):
    l = list(input())
    C.append(["#"] + l)

q = deque([start])
C[start[0]][start[1]] = 0
while q:
    now = q.popleft()
    for action in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        pos = [now[0]+action[0], now[1]+action[1]]
        if C[pos[0]][pos[1]] == "#":
            continue
        elif C[pos[0]][pos[1]] == ".":
            C[pos[0]][pos[1]] = C[now[0]][now[1]] + 1
            q.append(pos)
        else:
            if C[pos[0]][pos[1]] > C[now[0]][now[1]] + 1:
                C[pos[0]][pos[1]] = C[now[0]][now[1]] + 1
                q.append(pos)

print(C[goal[0]][goal[1]])