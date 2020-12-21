N = int(input())
P = list(map(int, input().split()))

max_num = max(P)
result = []

while True:
    max_index = P.index(max(P))
    result += [i+1 for i in range(max_index, len(P)-1)]
    del P[max_index]
    if [x for x in set(result) if result.count(x) > 1] != []:
        print(-1)
        break
    if P == []:
        for item in result:
            print(item)
        break