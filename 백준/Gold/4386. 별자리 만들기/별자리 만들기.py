import sys, math
input = sys.stdin.readline


def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
        return rep[x]
    else:
        return x


def union(x, y):
    if x > y:
        x, y = y, x
    rep[find_set(y)] = find_set(x)


n = int(input())
rep = [i for i in range(n)]
star_x = [None] * n
star_y = [None] * n
for i in range(n):
    star_x[i], star_y[i] = map(float, input().split())

dist = []
for i in range(n):
    for j in range(i+1, n):
        distance = math.sqrt((star_x[j] - star_x[i])**2+(star_y[j] - star_y[i])**2)
        dist.append((distance, i, j))
dist.sort(key=lambda x: x[0])

result = 0
for d in dist:
    distance, a, b = d
    if find_set(a) != find_set(b):
        result += distance
        union(a, b)

print(f"{result:.2f}")
