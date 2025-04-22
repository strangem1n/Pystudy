import sys
input = sys.stdin.readline


def date_to_int(month, day):
    result = day
    for k in range(1, month):
        result += max_day[k]
    return result


max_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())
flower = [[0, 0] for _ in range(n)]
for i in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start = date_to_int(start_month, start_day)
    end = date_to_int(end_month, end_day)
    flower[i][0], flower[i][1] = start, end-1
flower.sort(key=lambda x: (-x[1], x[0]))
used = [0] * n

want_start = date_to_int(2, 28)
want_end = date_to_int(11, 30)
cnt = 0
while want_start < want_end:
    for i in range(n):
        if used[i] == 1:
            continue

        flower_start, flower_end = flower[i]
        if flower_start-1 <= want_start < flower_end:
            want_start = flower_end
            cnt += 1
            used[i] = 1
            break
    else:
        cnt = 0
        break
print(cnt)
