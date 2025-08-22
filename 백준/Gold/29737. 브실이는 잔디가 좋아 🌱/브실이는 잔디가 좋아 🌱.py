import sys
input = sys.stdin.readline

def solve(record):
    idx = 0
    strick = []
    fail = 0
    while idx < len(record):
        if record[idx] == "O":
            start = idx
            used = 0
            length = 0
            last_strick_stack = 0
            last_strick = False
            while idx < len(record):
                if record[idx] == "O":
                    length += 1
                    last_strick_stack = 0
                    last_strick = False
                elif record[idx] == "X":
                    if last_strick:
                        last_strick = False
                        used -= last_strick_stack
                    fail += 1
                    break
                else:
                    used += 1
                    last_strick_stack += 1
                    last_strick = True
                idx += 1
            if last_strick:
                used -= last_strick_stack
            strick.append([length, used, start])
            continue
        elif record[idx] == "X":
            fail += 1
        idx += 1
    strick.sort(key=lambda x: (-x[0], x[1], x[2]))
    if not strick:
        strick.append([0, 0, 0])
    strick[0].append(fail)
    return strick[0]

n, w = map(int, input().split())
solved = []
for _ in range(n):
    nickname = input().rstrip()
    arr = [input().rstrip() for _ in range(7)]
    day = ""
    for i in range(w):
        for j in range(7):
            day += arr[j][i]
    solved.append(solve(day) + [nickname])
solved.sort(key=lambda x: (-x[0], x[1], x[2], x[3], x[4]))

solved[0].append(1)
rank = 1
for i in range(1, n):
    if solved[i][0] == solved[i-1][0] and solved[i][1] == solved[i-1][1] and solved[i][2] == solved[i-1][2] and solved[i][3] == solved[i-1][3]:
        pass
    else:
        rank += 1
    solved[i].append(rank)

for i in range(n):
    print(f"{solved[i][-1]}. {solved[i][-2]}")