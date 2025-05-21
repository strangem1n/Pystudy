import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * n
for i in range(1, n):
    cnt[i] = max(0, cnt[i-1]+math.ceil(math.log2(arr[i-1]/arr[i])))
print(sum(cnt))
