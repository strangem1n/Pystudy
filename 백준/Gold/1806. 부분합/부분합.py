import sys
input = sys.stdin.readline

n, s = map(int, input().split())
min_length = n + 1
arr = list(map(int, input().split()))
arr.append(0)

left = right = temp = 0
while right <= n:
    temp += arr[right]
    right += 1
    if temp >= s:
        if min_length > right - left:
            min_length = right - left
        while left < right:
            temp -= arr[left]
            left += 1
            if temp >= s and min_length > right - left:
                min_length = right - left
            elif temp < s:
                break

if min_length == n+1:
    print(0)
else:
    print(min_length)