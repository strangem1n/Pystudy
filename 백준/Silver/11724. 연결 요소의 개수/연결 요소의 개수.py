import sys
input = sys.stdin.readline

edge, node = map(int, input().split())

adj = [[] for _ in range(edge+1)]    # 각 정점을 인덱스로 하여 그 정점과 연결된 정점을 기록할 리스트

for _ in range(node):
    p1, p2 = map(int, input().split())
    adj[p1].append(p2)    # 방향이 없기 때문에 p1->p2,
    adj[p2].append(p1)    # p2->p1을 모두 기록

stack = [0] * (edge+1)    # DFS 탐색을 위한 스택
visited = [0] * (edge+1)    # 방문 기록
result = 0

# 한 지점에서 시작해서 갈 수 있는 만큼 쭉 가면서 방문을 기록함.
# 더 갈 수 있는 곳이 없으면 하나의 연결 요소가 끝났으므로 아직 방문하지 않은 지점 중 새로운 연결 요소를 시작점으로 함
for i in range(1, edge+1):
    if visited[i] == 0:
        result += 1    # 연결 요소의 개수
        top = 0
        stack[top] = i
        visited[i] = 1
        while top > -1:
            point = stack[top]    # 스택에서 하나 꺼내서 이 지점과 연결된 지점 탐색
            connect = adj[point]
            for p in connect:
                if visited[p] == 0:    # 연결된 곳 중 방문 기록 없는 곳이면 그곳으로 이동
                    top += 1
                    stack[top] = p
                    visited[p] = 1
                    break    # 이동한 곳에서 새롭게 시작
            else:    # 이 지점에서 더 이상 갈 수 있는 곳이 없으면 스택에서 하나 더 꺼냄(되돌아가기)
                top -= 1

print(result)
