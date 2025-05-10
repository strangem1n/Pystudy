import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    hi, hj = map(int, input().split())
    ci = [0] * n
    cj = [0] * n
    visited = [0] * n
    for k in range(n):
        ci[k], cj[k] = map(int, input().split())
    fi, fj = map(int, input().split())

    q = deque([[hi, hj]])
    success = False
    while q:
        i, j = q.popleft()
        if abs(i-fi) + abs(j-fj) <= 1000:
            success = True
            break
        for k in range(n):
            if visited[k] == 0 and abs(i-ci[k]) + abs(j-cj[k]) <= 1000:
                visited[k] = 1
                q.append([ci[k], cj[k]])
    if success:
        print('happy')
    else:
        print('sad')
