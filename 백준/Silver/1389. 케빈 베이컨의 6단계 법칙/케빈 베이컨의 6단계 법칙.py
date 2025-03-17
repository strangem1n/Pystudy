def bfs(num, n):
    visited = [0] * (n+1)
    front = rear = -1
    rear += 1
    queue[rear] = num
    visited[num] = 1
    while front != rear:
        front += 1
        current = queue[front]
        for friend in connect[current]:
            if visited[friend] == 0:
                rear += 1
                queue[rear] = friend
                visited[friend] = visited[current] + 1
    return sum(visited) - n


user, relation = map(int, input().split())
connect = [[] for _ in range(user+1)]
queue = [0] * user

for _ in range(relation):
    a, b = map(int, input().split())
    if b not in connect[a]:
        connect[a].append(b)
    if a not in connect[b]:
        connect[b].append(a)

min_num = 100 * 99
result = -1
for i in range(1, user+1):
    kevin = bfs(i, user)
    if min_num > kevin:
        min_num = kevin
        result = i
print(result)
