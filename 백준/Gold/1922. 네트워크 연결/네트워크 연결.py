import sys
input = sys.stdin.readline


def find_set(x):
    if rep[x] != x:
        rep[x] = find_set(rep[x])
        return rep[x]

    else:
        return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

n = int(input())
m = int(input())
rep = [i for i in range(n+1)]
v = [list(map(int, input().split())) for _ in range(m)]
v.sort(key=lambda x: x[2])

result = 0
cnt = 0
for i in range(m):
    n1, n2, cost = v[i]
    if find_set(n1) != find_set(n2):
        result += cost
        cnt += 1
        union(n1, n2)
print(result)