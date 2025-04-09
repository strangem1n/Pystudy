import sys
input = sys.stdin.readline


def find(a):
    if rep[a] != a:
        rep[a] = find(rep[a])
    return rep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        rep[b] = a
    else:
        rep[a] = b


p = int(input())
planet = [None] * p
for i in range(p):
    xi, yi, zi = list(map(int, input().split()))
    planet[i] = [xi, yi, zi, i]

rep = [i for i in range(p)]
vector = []

planet.sort(key=lambda x: x[0])
for i in range(p-1):
    vector.append([abs(planet[i+1][0] - planet[i][0]), planet[i+1][3], planet[i][3]])

planet.sort(key=lambda x: x[1])
for i in range(p-1):
    vector.append([abs(planet[i+1][1] - planet[i][1]), planet[i+1][3], planet[i][3]])

planet.sort(key=lambda x: x[2])
for i in range(p-1):
    vector.append([abs(planet[i+1][2] - planet[i][2]), planet[i+1][3], planet[i][3]])

vector.sort(key=lambda x: x[0])

total_cost = 0
cnt = 0
for vec in vector:
    if cnt == p-1:
        break
    cost, i, j = vec
    if find(i) != find(j):
        cnt += 1
        total_cost += cost
        union(i, j)
print(total_cost)
