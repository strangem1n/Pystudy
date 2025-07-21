import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
need = list(map(int, input().split()))
get = list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

in_queue = [False] * (n+1)
got = [False] * (n+1)
pq = []
for start in adj[r]:
    heapq.heappush(pq, [need[start-1], start])
    in_queue[start] = True
got[r] = True

result = get[r-1]
while pq:
    min_need, node = heapq.heappop(pq)
    if got[node]:
        continue
        
    if result >= min_need:
        result += get[node-1]
        got[node] = True
        for next_node in adj[node]:
            if not got[next_node] and not in_queue[next_node]:
                heapq.heappush(pq, [need[next_node-1], next_node])
                in_queue[next_node] = True
    else:
        break
print(result)