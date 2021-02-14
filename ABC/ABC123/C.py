
N = int(input())
num_list = []
for i in range(5):
    num_list.append(int(input()))
min_num = min(num_list)

if N%min_num == 0:
    res = 4 + N//min_num
else:
    res = 4 + N//min_num + 1
print(res)
