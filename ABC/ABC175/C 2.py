X, K, D = map(int, input().split())

if abs(X) - K*D > 0:
    print(abs(X) - K*D)
else:
    count = abs(X) // D
    dis = abs(X) % D
    if abs(dis-D) < dis:
        count += 1
        dis = abs(dis-D)
    K_count = K - count
    if K_count % 2 == 0:
        print(dis)
    else:
        print(abs(dis-D))