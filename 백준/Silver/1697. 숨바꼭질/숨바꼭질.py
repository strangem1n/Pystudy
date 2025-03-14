from collections import deque


def hide_and_seek(subin, baby):
    q = deque()
    q.append(subin)
    visited = [0] * 200001
    while q:
        current = q.popleft()
        if current == baby:
            return visited[current]

        teleport = current * 2
        walk_minus = current - 1
        walk_plus = current + 1

        if 0 < teleport < 200001 and visited[teleport] == 0:
            visited[teleport] = visited[current] + 1
            q.append(teleport)
        if 0 <= walk_minus < 200001 and visited[walk_minus] == 0:
            visited[walk_minus] = visited[current] + 1
            q.append(walk_minus)
        if 0 <= walk_plus < 200001 and visited[walk_plus] == 0:
            visited[walk_plus] = visited[current] + 1
            q.append(walk_plus)


n, k = map(int, input().split())
result = hide_and_seek(n, k)
print(result)
