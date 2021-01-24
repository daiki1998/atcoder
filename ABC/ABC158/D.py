from collections import deque

S = deque(list(input()))
Q = int(input())
Query = []

for _ in range(Q):
    Query.append(list(input().split()))
flag = True
for i in range(Q):
    if Query[i][0] == "1":
        if flag:
            flag = False
        else:
            flag = True
    else:
        if Query[i][1] == "1":
            if flag:
                S.appendleft(Query[i][2])
            else:
                S.append(Query[i][2])
        else:
            if flag:
                S.append(Query[i][2])
            else:
                S.appendleft(Query[i][2])
if flag == False:
    S.reverse()
print("".join(list(S)))