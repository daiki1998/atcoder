N = int(input())

res = 0
for i in range(1, N+1):
    num_i = (N//i)
    max_i = num_i*i
    min_i = i
    res += num_i * (max_i+min_i)//2
print(res)