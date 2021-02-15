from itertools import permutations, combinations_with_replacement

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

ABC = ["A", "B", "C"]
ABC_res = [A, B, C]
res = 10**9
for i in range(2**N):
    now_list = []
    for j in range(N):
        if ((i>>j)&1):
            now_list.append(l[j])
    for comb in combinations_with_replacement(ABC, len(now_list)):
        if len(set(comb)) < 3:
            continue
        for comb_jun in permutations(comb, len(comb)):
            A_B_C = [[],[],[]]
            for j, c in enumerate(comb_jun):
                if c == "A":
                    A_B_C[0].append(j)
                elif c == "B":
                    A_B_C[1].append(j)
                else:
                    A_B_C[2].append(j)
            cnt = 0

            for j in range(3):
                if len(A_B_C[j]) >= 2:
                    cnt_ABC = 0
                    for k in A_B_C[j]:
                        cnt_ABC += now_list[k]
                    cnt += abs(ABC_res[j] - cnt_ABC) + (len(A_B_C[j])-1)*10
                else:
                    cnt += abs(ABC_res[j] - now_list[A_B_C[j][0]])
            res = min(res, cnt)
print(res)
