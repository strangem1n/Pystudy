def solution(wallpaper):
    r = len(wallpaper)
    c = len(wallpaper[0])
    min_r, max_r = r, 0
    min_c, max_c = c, 0
    for i in range(r):
        for j in range(c):
            if wallpaper[i][j] == '#':
                min_r = min(min_r, i)
                max_r = max(max_r, i+1)
                min_c = min(min_c, j)
                max_c = max(max_c, j+1)
    answer = [min_r, min_c, max_r, max_c]
    return answer