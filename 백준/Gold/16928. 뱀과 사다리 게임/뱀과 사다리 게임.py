def game():
    front = rear = -1
    rear += 1
    queue[rear] = 1

    while front != rear:
        front += 1
        current = queue[front]
        for dice in range(6, 0, -1):
            forward = current + dice
            for move in range(stair + snake):
                if forward == start[move]:
                    forward = end[move]
                    break
            if forward == 100:
                return visited[current] + 1
            elif forward < 100 and visited[forward] == 0:
                visited[forward] = visited[current] + 1
                rear += 1
                queue[rear] = forward


stair, snake = map(int, input().split())
start = [0] * (stair+snake)
end = [0] * (stair+snake)
for i in range(stair+snake):
    start[i], end[i] = map(int, input().split())

queue = [0] * 101
visited = [0] * 101
print(game())
