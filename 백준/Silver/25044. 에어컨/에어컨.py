import sys
n, k = map(int, sys.stdin.readline().split())

arr = [None] * (3 * (n+1))
for i in range(n+1):
    arr[3*i] = [i, 15, i*k]
    arr[3*i+1] = [i, 18, i*k]
    arr[3*i+2] = [i, 21, i*k]

result = []
for i in range(len(arr)):
    while arr[i][2] >= 60:
        arr[i][1] += 1
        arr[i][2] -= 60
    while arr[i][1] >= 24:
        arr[i][0] += 1
        arr[i][1] -= 24
    if arr[i][0] == n:
        result.append(arr[i])

print(len(result))
for res in result:
    h = str(res[1])
    m = str(res[2])
    h = '0'+h if len(h) == 1 else h
    m = '0'+m if len(m) == 1 else m
    print(f"{h}:{m}")
