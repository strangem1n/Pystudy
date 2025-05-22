import sys
from bisect import bisect_left
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))

        lis = [arr[0]]
        for i in range(1, n):
            if lis[-1] < arr[i]:
                lis.append(arr[i])
            else:
                lis[bisect_left(lis, arr[i])] = arr[i]
        print(len(lis))
    except:
        break
