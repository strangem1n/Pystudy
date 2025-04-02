import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
prefix_arr = [0] * (N+1)
prefix_arr[1] = arr[0]
for i in range(2, N+1):
    prefix_arr[i] = arr[i-1] + prefix_arr[i-1]
M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(prefix_arr[y] - prefix_arr[x-1])
