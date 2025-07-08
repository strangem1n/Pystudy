import sys, heapq
input = sys.stdin.readline

n, centi, t = map(int, input().split())
giant = []
for _ in range(n):
    heapq.heappush(giant, -int(input()))

for cnt in range(t+1):
    biggest = -heapq.heappop(giant)
    if biggest < centi:
        print('YES')
        print(cnt)
        break
    if biggest > 1:
        heapq.heappush(giant, -(biggest // 2))
    else:
        print('NO')
        print(1)
        break
else:
    print('NO')
    print(biggest)