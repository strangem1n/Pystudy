import sys
input = sys.stdin.readline


# 왼쪽으로 이동
def move(board):
    fixed = [[0] * n for _ in range(n)]
    i = 0
    while i < n:
        j = 1
        while j < n:
            if board[i][j] == 0:
                j += 1
            else:
                if board[i][j-1] == 0:
                    board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
                    if j > 1:
                        j -= 1
                elif board[i][j-1] == board[i][j] and fixed[i][j-1] == 0:
                    board[i][j], board[i][j-1] = 0, board[i][j-1]*2
                    fixed[i][j-1] = 1
                else:
                    j += 1
        i += 1


def find_max(arr):
    max_n = 0
    for i in range(n):
        for j in range(n):
            if max_n < arr[i][j]:
                max_n = arr[i][j]
    return max_n


def game(arr, cnt):
    global max_num
    if cnt == 5:
        num = find_max(arr)
        max_num = max(max_num, num)
    else:
        copy_arr_left = [a[:] for a in arr]
        copy_arr_right = [a[::-1] for a in arr]
        copy_arr_up = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                copy_arr_up[i][j] = copy_arr_right[j][i]
        copy_arr_down = [a[::-1] for a in copy_arr_up]

        move(copy_arr_left)
        move(copy_arr_right)
        move(copy_arr_up)
        move(copy_arr_down)

        game(copy_arr_left, cnt+1)
        game(copy_arr_right, cnt+1)
        game(copy_arr_up, cnt+1)
        game(copy_arr_down, cnt+1)


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
game(array, 0)
print(max_num)
