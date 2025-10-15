import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ground = list(map(int, input().split()))
command = [0] * (n + 1)
for _ in range(m):
    a, b, k = map(int, input().split())
    command[a-1] += k
    command[b] -= k

add = 0
for i in range(n):
    add += command[i]
    print(ground[i] + add, end=" ")
