di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def solution(maps):
    r = len(maps)
    c = len(maps[0])

    maps = [list(map(lambda x: 0 if x == 'X' else int(x), m)) for m in maps]
    
    answer = []
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 0:
                res = 0
                stack = [(i, j)]
                while stack:
                    i, j = stack[-1]
                    res += maps[i][j]
                    maps[i][j] = 0
                    for k in range(4):
                        ni, nj = i+di[k], j+dj[k]
                        if 0 <= ni < r and 0 <= nj < c and maps[ni][nj] > 0:
                            stack.append((ni, nj))
                            break
                    else:
                         stack.pop()   
                answer.append(res)
    if not answer:
        return [-1]
    answer.sort()
    return answer