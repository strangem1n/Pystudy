n, m = map(int, input().split())

xi = [0] * n
yi = [0] * n
dist = [0] * n

x = y = 0

for i in range(n):
    xi[i], yi[i] = map(int, input().split())
    dist[i] = (x-xi[i])**2 + (y-yi[i])**2

result = 0
for _ in range(m):
    max_dist = idx = 0
    for k in range(n):
        if max_dist < dist[k]:
            max_dist = dist[k]
            idx = k
    result += max_dist
    x, y = xi[idx], yi[idx]
    xi[idx], yi[idx] = map(int, input().split())
    for i in range(n):
        dist[i] = (x-xi[i])**2 + (y-yi[i])**2

print(result)