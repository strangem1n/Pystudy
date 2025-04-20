n = int(input())
dasom = int(input())
arr = [0] + [int(input()) for _ in range(n-1)]
arr.sort()

cnt = 0
while dasom <= arr[-1]:
    dasom += 1
    arr[-1] -= 1
    cnt += 1

    for i in range(n-1, -1, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        else:
            break
print(cnt)
