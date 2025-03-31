def f(cnt, previous_i):
    if cnt == m:
        if seq[:] not in result:
            result.append(seq[:])
    else:
        for i in range(previous_i+1, n):
            if visited[i] == 0:
                visited[i] = 1
                seq[cnt] = arr[i]
                f(cnt+1, i)
                visited[i] = 0


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * n
seq = [0] * m
result = []
f(0, -1)
for seq in result:
    print(*seq)
