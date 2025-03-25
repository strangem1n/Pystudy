n, k = map(int, input().split())
arr = [i for i in range(2, n+1)]

min_idx = 0
remove_cnt = 0
result = 0
while remove_cnt < k:
    while arr[min_idx] == 0:
        min_idx += 1
    prime = arr[min_idx]
    for i in range(n-1):
        if arr[i] != 0 and arr[i] % prime == 0:
            result = arr[i]
            arr[i] = 0
            remove_cnt += 1
            if remove_cnt == k:
                break

print(result)