import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
level = [0] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    level[b] += 1

pq = []
for i in range(1, n+1):
    if level[i] == 0:
        heapq.heappush(pq, i)

while pq:
    num = heapq.heappop(pq)
    for next_n in adj[num]:
        level[next_n] -= 1
        if level[next_n] == 0:
            heapq.heappush(pq, next_n)
    print(num, end=" ")
