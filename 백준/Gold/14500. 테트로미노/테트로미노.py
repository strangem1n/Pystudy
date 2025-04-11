import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_result = 0

for i in range(n):
    for j in range(m):
        try:
            max_result = max(max_result, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j])
        except IndexError:
            pass

        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1])
        except IndexError:
            pass

        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i+2][j])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+2]+arr[i+1][j+2]+arr[i+1][j+1]+arr[i+1][j])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i][j+1])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i][j])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i][j+2])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+2]+arr[i+1][j+2]+arr[i][j+1]+arr[i][j])
        except IndexError:
            pass

        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j]+arr[i+2][j])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+2]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j])
        except IndexError:
            pass

        try:
            max_result = max(max_result, arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i][j+2])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i+1][j]+arr[i+1][j+1]+arr[i][j+1]+arr[i+1][j+2])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j])
        except IndexError:
            pass
        try:
            max_result = max(max_result, arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j]+arr[i+2][j+1])
        except IndexError:
            pass

print(max_result)
