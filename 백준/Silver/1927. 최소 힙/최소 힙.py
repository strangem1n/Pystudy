import heapq
import sys
input = sys.stdin.readline

q = []
len_q = 0

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len_q == 0:
            print(0)
        else:
            result = heapq.heappop(q)
            len_q -= 1
            print(result)
    else:
        len_q += 1
        heapq.heappush(q, x)
