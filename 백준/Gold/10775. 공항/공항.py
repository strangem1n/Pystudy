import sys
input = sys.stdin.readline

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
        return parent[x]
    else:
        return x

def union(x, y):
    a = parent[x]
    b = parent[y]
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())
airplane = [int(input()) for _ in range(p)]
parent = [i for i in range(g+1)]

for i in range(p):
    airport = find_set(airplane[i])
    if airport > 0:
        union(airport-1, airplane[i])
    else:
        print(i)
        break
else:
    print(p)
