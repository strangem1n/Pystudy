def solve(num):
    for chk in range(num, 0, -1):
        cnt = 0
        for k in range(num):
            if arr_min[k] <= chk <= arr_max[k]:
                cnt += 1
        if cnt == chk:
            return cnt
    return -1


n = int(input())
arr_min = [0] * n
arr_max = [0] * n
for i in range(n):
    arr_min[i], arr_max[i] = map(int, input().split())
print(solve(n))
