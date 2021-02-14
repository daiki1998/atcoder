
A, B, C = map(int, input().split())

if B+C >= A:
    print(C-(A-B))
else:
    print(0)