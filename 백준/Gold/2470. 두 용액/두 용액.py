import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
if arr[-1] <= 0:
    print(arr[-2], arr[-1])
elif arr[0] >= 0:
    print(arr[0], arr[1])
else:
    a = b = 0
    min_diff = float('inf')
    for i in range(n):
        res = bisect.bisect_left(arr, -arr[i])
        if i < res:
            res -= 1
        if arr[i] == arr[res]:
            continue
        if min_diff > abs(arr[i] + arr[res]):
            min_diff = abs(arr[i] + arr[res])
            if arr[i] < arr[res]:
                a, b = arr[i], arr[res]
            else:
                a, b = arr[res], arr[i]
            if min_diff == 0:
                break
    print(a, b)