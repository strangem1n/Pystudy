import sys
input = sys.stdin.readline

def slope(si, sj, kind):
    is_slope = [0] * n
    if kind == 0:
        while sj < n-1:
            sj += 1
            if arr[si][sj] == arr[si][sj-1]:
                continue
            elif arr[si][sj] - arr[si][sj-1] == 1:
                prev = arr[si][sj-1]
                for k in range(l):
                    if sj-1-k < 0 or is_slope[sj-1-k] == 1 or prev != arr[si][sj-1-k]:
                        return False
                    is_slope[sj-1-k] = 1
            elif arr[si][sj] - arr[si][sj-1] == -1:
                nex = arr[si][sj]
                for k in range(l):
                    if sj+k >= n or is_slope[sj+k] == 1 or nex != arr[si][sj+k]:
                        return False
                    is_slope[sj+k] = 1
            else:
                return False
    else:
        while si < n-1:
            si += 1
            if arr[si][sj] == arr[si-1][sj]:
                continue
            elif arr[si][sj] - arr[si-1][sj] == 1:
                prev = arr[si-1][sj]
                for k in range(l):
                    if si-1-k < 0 or is_slope[si-1-k] == 1 or prev != arr[si-1-k][sj]:
                        return False
                    is_slope[si-1-k] = 1
            elif arr[si][sj] - arr[si-1][sj] == -1:
                nex = arr[si][sj]
                for k in range(l):
                    if si+k >= n or is_slope[si+k] == 1 or nex != arr[si+k][sj]:
                        return False
                    is_slope[si+k] = 1
            else:
                return False
    return True


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    if slope(0, i, 1):
        result += 1
    if slope(i, 0, 0):
        result += 1
print(result)