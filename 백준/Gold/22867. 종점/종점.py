import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    s, e = input().split()
    start = [int(s[:2]), int(s[3:5]), int(s[6:8]), int(s[9:])]
    end = [int(e[:2]), int(e[3:5]), int(e[6:8]), int(e[9:])]

    start[1] += start[0] * 60
    end[1] += end[0] * 60

    start[2] += start[1] * 60
    end[2] += end[1] * 60

    start[3] += start[2] * 1000
    end[3] += end[2] * 1000

    heapq.heappush(pq, [start[3], 1])
    heapq.heappush(pq, [end[3], -1])

result = 0
max_result = 0
while pq:
    time, value = heapq.heappop(pq)
    result += value
    if max_result < result:
        max_result = result
print(max_result)