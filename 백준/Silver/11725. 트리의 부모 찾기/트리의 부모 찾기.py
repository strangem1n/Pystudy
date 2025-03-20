import sys, collections
input = sys.stdin.readline


def bfs():    # 1번 노드를 출발점으로 bfs
    q = collections.deque([1])
    visited[1] = 1
    while q:
        parent = q.popleft()
        for v in adj[parent]:
            if visited[v] == 0:    # 경로를 따라 내려가면서 다음 노드의 부모를 현재 노드로 저장
                q.append(v)
                rep[v] = parent
                visited[v] = 1


n = int(input())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
rep = [0] * (n+1)    # 각 노드의 부모 노드 저장

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bfs()
for i in range(2, n+1):
    print(rep[i])