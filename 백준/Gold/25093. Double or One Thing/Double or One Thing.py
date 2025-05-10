import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    word = input().rstrip()
    arr = [[ord(word[0]), 1]]
    for i in range(1, len(word)):
        if ord(word[i]) == arr[-1][0]:
            arr[-1][1] += 1
        else:
            arr.append([ord(word[i]), 1])

    for i in range(len(arr)-2, -1, -1):
        if arr[i][0] < arr[i+1][0]:
            arr[i][1] *= 2

    print(f'Case #{tc}: ', end='')
    for i in range(len(arr)):
        for j in range(arr[i][1]):
            print(chr(arr[i][0]), end='')
    print('')
