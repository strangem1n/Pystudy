di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    ni, nj = i+di[k], j+dj[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        if board[ni][nj] == 0:
                            board[ni][nj] = 2
                            
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer