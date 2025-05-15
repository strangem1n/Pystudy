import sys
input = sys.stdin.readline

n = int(input())
balls = list(map(int, input().split()))
sorted_balls = sorted(balls)

idx = -1
not_move = 0
for i in range(n-1, -1, -1):
    if balls[i] == sorted_balls[idx]:
        n -= 1
        idx -= 1

print(n)
