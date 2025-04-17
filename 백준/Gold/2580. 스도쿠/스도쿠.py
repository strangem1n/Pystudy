import sys
input = sys.stdin.readline


def f(cnt, lim):
    if cnt == lim + 1:
        for s in sudoku:
            print(*s)
        exit(0)
    else:
        r = blank_i[cnt]
        c = blank_j[cnt]
        can_fill_nums = blank_nums[cnt]
        for num in can_fill_nums:
            sudoku[r][c] = num
            if chk(r, c):
                f(cnt+1, lim)
            sudoku[r][c] = 0


def chk(r, c):
    available = [3] * 10

    for i in range(9):
        available[sudoku[i][c]] -= 1
        available[sudoku[r][i]] -= 1

    r = r - r % 3
    c = c - c % 3
    for nr in range(r, r+3):
        for nc in range(c, c+3):
            available[sudoku[nr][nc]] -= 1

    for i in range(1, 10):
        if available[i] < 0:
            return False
    return True


def fill(r, c):
    available = [1] * 10

    for i in range(9):
        available[sudoku[i][c]] -= 1
        available[sudoku[r][i]] -= 1

    r = r - r%3
    c = c - c%3
    for nr in range(r, r+3):
        for nc in range(c, c+3):
            available[sudoku[nr][nc]] -= 1

    nums = []
    for i in range(1, 10):
        if available[i] == 1:
            nums.append(i)
    return nums


sudoku = [list(map(int, input().split())) for _ in range(9)]
blank_i = [None] * 81
blank_j = [None] * 81
blank_nums = [None] * 81
top = -1
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            can_fill = fill(i, j)
            if len(can_fill) == 1:
                sudoku[i][j] = can_fill[0]
            else:
                top += 1
                blank_i[top] = i
                blank_j[top] = j
                blank_nums[top] = can_fill

f(0, top)
