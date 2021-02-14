
N = int(input())
W = list(map(int, input().split()))

sum_w = sum(W)
sum_T = 0
abs_sum = 10000
i = 0
while True:
    sum_T += W[i]
    if abs(sum_T - sum_w/2) < abs_sum:
        abs_sum = abs(sum_T - sum_w/2)
    else:
        sum_T -= W[i]
        index = i
        break
    i += 1

print(abs(sum(W[:index]) - sum(W[index:])))