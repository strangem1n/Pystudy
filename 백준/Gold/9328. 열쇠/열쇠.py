import sys
from collections import deque
input = sys.stdin.readline

def chk(r, c, queue, tem, vis, ans):
    vis[r][c] = 1
    if arr[r][c] == '.':
        queue.append([r, c])
    elif arr[r][c] == '$':
        ans += 1
        queue.append([r, c])
    elif arr[r][c] != '*':
        if ord(arr[r][c]) < 91:  # 대문자: 문
            ab = ord(arr[r][c]) - 65
            if have_key[ab] == 1:
                queue.append([r, c])
            else:
                tem[ab].append([r, c])
        else:  # 소문자: 열쇠
            queue.append([r, c])
            ab = ord(arr[r][c]) - 97
            if have_key[ab] == 0:
                have_key[ab] = 1
                queue.extend(tem[ab])
    return queue, tem, vis, ans

def bfs():
    get_doc = 0
    q = deque([])
    visited = [[0] * m for _ in range(n)]
    temp = [[] for _ in range(26)]
    for i in range(0, n, n-1):
        for j in range(m):
            q, temp, visited, get_doc = chk(i, j, q, temp, visited, get_doc)

    for i in range(1, n-1):
        for j in range(0, m, m-1):
            q, temp, visited, get_doc = chk(i, j, q, temp, visited, get_doc)

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0:
                q, temp, visited, get_doc = chk(ni, nj, q, temp, visited, get_doc)
    return get_doc

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [input().rstrip() for _ in range(n)]
    key = input().rstrip()
    have_key = [0] * 26
    if key == '0':
        pass
    else:
        for ki in key:
            have_key[ord(ki)-97] = 1
    result = bfs()
    print(result)
