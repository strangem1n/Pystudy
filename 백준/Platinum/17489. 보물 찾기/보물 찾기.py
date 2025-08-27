import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, j, cnt, w):
    global word_cnt, ti, tj
    if word_cnt <= w and cnt == l-1:
        word_cnt = w + 1
        ti, tj = i, j

    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            next_cnt = (cnt + 1) % l
            if arr[ni][nj] == word[next_cnt]:
                if visited[ni][nj] == next_cnt:
                    print(-1)
                    exit(0)

                visited[ni][nj] = next_cnt
                if next_cnt == 0:
                    dfs(ni, nj, next_cnt, w+1)
                else:
                    dfs(ni, nj, next_cnt, w)
                visited[ni][nj] = -1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

n, m, l = map(int, input().split())
word = input().rstrip()
arr = [input().rstrip() for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
word_cnt = ti = tj = 0
dfs(0, 0, 0, 0)

if word_cnt > 0:
    print(word_cnt)
    print(ti+1, tj+1)
else:
    print(-1)