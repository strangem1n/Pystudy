import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    level = [0] * (n+1)
    prev = [set() for __ in range(n+1)]
    for i in range(1, n):
        level[arr[i]] = i
        for j in range(i):
            prev[arr[i]].add(arr[j])

    swap = int(input())
    for s in range(swap):
        a, b = map(int, input().split())
        if level[a] > level[b]:
            prev[a].discard(b)
            prev[b].add(a)
        else:
            prev[b].discard(a)
            prev[a].add(b)

    result = [None] * n
    for i in range(1, n+1):
        result[i-1] = (len(prev[i]), i)
    result.sort()

    ans = []
    for i in range(n):
        if result[i][0] == i:
            ans.append(result[i][1])
        else:
            print('IMPOSSIBLE')
            break
    else:
        print(*ans)