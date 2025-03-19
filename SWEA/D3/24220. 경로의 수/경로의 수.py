def dfs(start, end):    # 재귀로 DFS 구현
    global result
    if start == end:    # 도착하면 경로 +1
        result += 1
    else:
        for middle in adj[start]:    # 현 지점에서 갈 수 있는 곳 탐색
            if visited[middle] == 0:
                visited[middle] = 1
                dfs(middle, end)
                visited[middle] = 0


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (N+1)
    S, G = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for i in range(E):
        adj[arr[i*2]].append(arr[i*2+1])    # 방향성 있는 그래프

    result = 0
    dfs(S, G)
    print(f"#{tc} {result}")
