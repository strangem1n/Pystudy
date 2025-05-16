import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])
arr = list(map(int, input().split()))
for i in range(1, n+1):
    if arr[-i] == 1:
        q.appendleft(i)
    elif arr[-i] == 2:
        temp = q.popleft()
        q.appendleft(i)
        q.appendleft(temp)
    else:
        q.append(i)

print(*q)
