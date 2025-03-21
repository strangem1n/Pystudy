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
            len_q -= 1
            result = heapq.heappop(q)
            if result % 2 == 1:
                result = (result + 1)//2 * -1
            else:
                result //= 2
            print(result)
    else:
        len_q += 1
        if x < 0:
            x = -x * 2 - 1
        else:
            x *= 2
        heapq.heappush(q, x)
