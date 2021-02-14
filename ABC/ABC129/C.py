
N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(int(input()))
S = set(A)
dp = [0 for i in range(N+1)]
dp[0] = 1
mod = 1000000007
for now in range(N):
    for next_num in range(now+1, now+3):
        if next_num > N:
            continue
        else:
            if next_num not in S:
                dp[next_num] += dp[now]
                dp[next_num] %= mod
print(dp[-1])