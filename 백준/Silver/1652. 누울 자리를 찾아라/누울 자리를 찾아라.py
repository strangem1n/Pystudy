n = int(input())
arr = [input() for _ in range(n)]
w_cnt = h_cnt = 0

for i in range(n):
    j = -1
    subset = 0
    while j < n-1:
        j += 1
        if arr[i][j] == '.':
            subset += 1
        else:
            if subset > 1:
                w_cnt += 1
            subset = 0
    if subset > 1:
        w_cnt += 1



for j in range(n):
    i = -1
    subset = 0
    while i < n-1:
        i += 1
        if arr[i][j] == '.':
            subset += 1
        else:
            if subset > 1:
                h_cnt += 1
            subset = 0
    if subset > 1:
        h_cnt += 1

print(w_cnt, h_cnt)
