import sys
input = sys.stdin.readline

def binary_search(num):
    start = 0
    end = n-1
    while start < end:
        if end == start + 1:
            if abs(num + arr[start]) < abs(num + arr[end]):
                return start
            else:
                return end
        middle = (start + end) // 2
        if num + arr[middle] == 0:
            return middle
        elif num + arr[middle] > 0:
            end = middle
        else:
            start = middle + 1
    return middle

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
        res = binary_search(arr[i])
        if i == res:
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