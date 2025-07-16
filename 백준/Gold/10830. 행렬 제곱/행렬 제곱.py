import sys
input = sys.stdin.readline

def power(array1, array2):
    new_array = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_array[i][j] += array1[i][k] * array2[k][j]
            new_array[i][j] %= 1000
    return new_array

def divide(array, cnt):
    if cnt == 1:
        return array
    elif cnt == 2:
        return power(array, array)
    else:
        middle = divide(array, cnt // 2)
        if cnt % 2 == 0:
            return power(middle, middle)
        else:
            return power(power(middle, middle), arr)


n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] %= 1000

result = divide(arr, b)
for r in result:
    print(*r)