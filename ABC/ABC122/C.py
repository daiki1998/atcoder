import bisect
from collections import defaultdict

N, Q = map(int, input().split())
S = input()
S_AC = []
for i in range(N-1):
    if S[i:i+2] == "AC":
        S_AC.append(i+1)
dp = defaultdict(lambda: -1)
for _ in range(Q):
    l, r = map(int, input().split())
    if dp[l] != -1:
        l_index = dp[l]
    else:
        l_index = bisect.bisect_left(S_AC, l)
        dp[l] = l_index
    if dp[r] != -1:
        r_index = dp[r]
    else:
        r_index = bisect.bisect_left(S_AC, r)
        dp[r] = r_index
    print(r_index-l_index)
