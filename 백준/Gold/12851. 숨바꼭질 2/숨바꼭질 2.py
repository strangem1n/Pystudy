from collections import deque

def bfs(start, end):
    if start == end:    # 예외처리
        return 0, 1

    q = deque([start])
    visited[start] = 1
    cnt = 0
    min_time = 100002

    while q:
        middle = q.popleft()
        # 가지치기: 큐에서 꺼낸 값이 저장된 최소 시간보다 길면 (그래프의 다음 레벨로 넘어가버리면) 종료
        if visited[middle] > min_time-1:    #
            break
        arr = [middle+1, middle-1, middle*2]
        for a in arr:
            # 바로 종료하는 게 아니라, 다른 가지에서도 같은 시간(가장 빠른 시간)으로 도착할 수 있는지 큐에 저장된 값을 꺼내서 계속 탐색
            if a == end:
                cnt += 1
                min_time = visited[middle] + 1
            # 아직 방문하지 않았거나, 여기까지 오는 데 걸린 시간이 같아야 큐에 넣어서 가지를 이어나갈 것임
            elif -1 < a < 200001 and (visited[a] == 0 or visited[a] == visited[middle]+1):
                q.append(a)
                visited[a] = visited[middle] + 1
    return min_time-1, cnt


n, k = map(int, input().split())
visited = [0] * 200001
result_time, result_cnt = bfs(n, k)
print(result_time)
print(result_cnt)
