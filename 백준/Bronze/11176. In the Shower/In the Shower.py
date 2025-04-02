T = int(input())
for _ in range(T):
    E, N = map(int, input().split())
    cnt = 0
    for i in range(N):
        if int(input()) > E:
            cnt += 1
    print(cnt)
