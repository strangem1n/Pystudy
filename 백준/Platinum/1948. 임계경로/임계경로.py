import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
level = [0] * (n+1)
cost = [0] * (n+1)
prev = [[] for _ in range(n+1)]
adj = [[] for _ in range(n+1)]

road_num = 0
for _ in range(m):
    start, end, c = map(int, input().split())
    adj[start].append([end, c, road_num])
    road_num += 1
    level[end] += 1

start, end = map(int, input().split())
q = deque([start])
while q:
    city = q.popleft()
    for next_city, next_cost, r in adj[city]:
        level[next_city] -= 1
        if cost[next_city] < cost[city] + next_cost:
            cost[next_city] = cost[city] + next_cost
            prev[next_city] = [[r, city]]
        elif cost[next_city] == cost[city] + next_cost:
            prev[next_city].append([r, city])
        if level[next_city] == 0:
            q.append(next_city)
print(cost[end])

result = set()
back = deque([])
for r, c in prev[end]:
    result.add(r)
    back.append(c)

chk = [False] * (n+1)
chk[start] = True
while back:
    city = back.popleft()
    for prev_road, prev_city in prev[city]:
        result.add(prev_road)
        if chk[prev_city]:
            continue
        back.append(prev_city)
        chk[prev_city] = True
print(len(result))