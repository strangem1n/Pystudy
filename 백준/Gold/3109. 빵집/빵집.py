import sys
input = sys.stdin.readline


def pipe(i, j):
    if j == c-1:
        return True

    else:
        if 0 <= i-1 and visited[i-1][j+1] == 0 and arr[i-1][j+1] == '.':
            visited[i-1][j+1] = 1
            if pipe(i-1, j+1):
                return True

        if visited[i][j+1] == 0 and arr[i][j+1] == '.':
            visited[i][j+1] = 1
            if pipe(i, j+1):
                return True

        if i+1 < r and visited[i+1][j+1] == 0 and arr[i+1][j+1] == '.':
            visited[i+1][j+1] = 1
            if pipe(i+1, j+1):
                return True

        return False


r, c = map(int, input().split())
arr = list(input().rstrip() for _ in range(r))
visited = [[0] * c for _ in range(r)]
result = 0
for y in range(r):
    visited[y][0] = 1
    if pipe(y, 0):
        result += 1
print(result)
