import sys
input = sys.stdin.readline

def dfs(i, j, cnt):
    global max_result
    max_result = max(max_result, cnt)
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < r and 0 <= nj < c and used[arr[ni][nj]] == 0:
            used[arr[ni][nj]] = 1
            dfs(ni, nj, cnt+1)
            used[arr[ni][nj]] = 0

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
arr = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
max_result = 0
used = [0] * 26
used[arr[0][0]] = 1
dfs(0, 0, 1)
print(max_result)
