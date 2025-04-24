import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

i = 0
result = 0
while i < n-1:
    if arr[i] < 0:
        if arr[i+1] < 0:
            result += arr[i]*arr[i+1]
            i += 2
        elif arr[i+1] == 0:
            i += 2
        elif arr[i+1] > 0:
            result += arr[i]
            i += 1
    elif arr[i] == 0:
        if arr[i+1] == 0:
            i += 2
        elif arr[i+1] > 0:
            i += 1
    elif arr[i] > 0:
        if (n-i) % 2 == 1:
            result += arr[i]
            i += 1
        else:
            result += max(arr[i]*arr[i+1], arr[i]+arr[i+1])
            i += 2

if i == (n-1):
    result += arr[i]
print(result)