import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * (n+1) for _ in range(n+1)]
sum_board = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    board[i][j] = 1
    sum_board[i][j] = 1

for i in range(n):
    for j in range(n):
        sum_board[i+1][j+1] += sum_board[i][j+1] + sum_board[i+1][j] - sum_board[i][j]

divisor = []
for i in range(1, m+1):
    if m % i == 0:
        divisor.append([i-1, m//i-1])

max_area = 0
for si in range(1, n+1):
    for sj in range(1, n+1):
        for pi, pj in divisor:
            ei, ej = si + pi, sj + pj
            if 1 <= ei < n+1 and 1 <= ej < n+1:
                block_in_area = sum_board[ei][ej] - sum_board[si-1][ej] - sum_board[ei][sj-1] + sum_board[si-1][sj-1]
                if max_area < block_in_area:
                    max_area = block_in_area
print(m-max_area)
