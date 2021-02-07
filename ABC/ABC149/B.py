
A, B, K = map(int, input().split())

res_A = max(0, A-K)
num = K-A if res_A == 0 else 0
res_B = max(0, B-num)
print(res_A, res_B)