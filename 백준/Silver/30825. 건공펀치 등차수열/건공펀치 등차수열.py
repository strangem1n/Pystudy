n, k = map(int, input().split())
arr = list(map(int, input().split()))

prev = arr[0]
cnt = 0
for i in range(1, n):
    if arr[i] <= prev + k:
        cnt += prev + k - arr[i]
        prev += k
    else:
        cnt += (arr[i] - (prev + k)) * i
        prev = arr[i]
print(cnt)
