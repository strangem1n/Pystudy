import heapq

n, k = map(int, input().split())
q = [(0, n)]
dij = [float("inf")] * 200001
dij[n] = 0
result = -1

while q:    # 우선순위 큐를 이용한 다익스트라 - bfs와 형태가 유사하다
    time, start = heapq.heappop(q)
    if start == k:
        result = time
        break

    if 0 < start*2 <= 100000 and time < dij[start*2]:
        dij[start*2] = time
        heapq.heappush(q, [time, start*2])
    if 0 <= start+1 < 200000 and time+1 < dij[start+1]:
        dij[start+1] = time+1
        heapq.heappush(q, [time+1, start+1])
    if 0 <= start-1 < 200000 and time+1 < dij[start-1]:
        dij[start-1] = time+1
        heapq.heappush(q, [time+1, start-1])

print(result)
