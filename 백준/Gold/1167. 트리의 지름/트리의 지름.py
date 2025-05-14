import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited = [0] * (v+1)
    visited[start] = 1
    while q:
        ver = q.popleft()
        for next_ver, dist in adj[ver]:
            if visited[next_ver] == 0:
                visited[next_ver] = visited[ver] + dist
                q.append(next_ver)
    max_dist = max(visited)
    for idx in range(1, v+1):
        if visited[idx] == max_dist:
            return idx, max_dist-1

v = int(input())
adj = [[] for _ in range(v+1)]
for _ in range(v):
    vertex, *nodes = map(int, input().split())
    for i in range(0, len(nodes), 2):
        node = nodes[i]
        if node == -1:
            break
        distance = nodes[i+1]
        adj[vertex].append((node, distance))

for i in range(v):
    if len(adj[i]) > 0:
        end1, temp = bfs(i)
        end2, diameter = bfs(end1)
        print(diameter)
        break
