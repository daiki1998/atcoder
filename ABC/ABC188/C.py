import copy

N = int(input())
A = [0] + list(map(int, input().split()))

index_list = [i for i in range(1, 2**N+1)]
if N != 1:
    while True:
        index = 0
        next_index_list = []
        for i in range(0, len(index_list), 2):
            if A[index_list[i]] > A[index_list[i+1]]:
                next_index_list.append(index_list[i])
            else:
                next_index_list.append(index_list[i+1])
        index_list = copy.deepcopy(next_index_list)
        if len(index_list) == 2:
            break
if A[index_list[0]] > A[index_list[1]]:
    print(index_list[1])
else:
    print(index_list[0])