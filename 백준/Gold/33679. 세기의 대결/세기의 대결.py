import sys
from bisect import bisect_left
from collections import deque
input = sys.stdin.readline

n = int(input())
yj = deque(map(int, input().split()))
hg = deque(map(int, input().split()))

max_yj = max_hg = 0
for _ in range(n):
    yj_lis = []
    hg_lis = []
    for i in range(n):
        yj_idx = bisect_left(yj_lis, yj[i])
        if yj_idx == len(yj_lis):
            yj_lis.append(yj[i])
        else:
            yj_lis[yj_idx] = yj[i]

        hg_idx = bisect_left(hg_lis, hg[i])
        if hg_idx == len(hg_lis):
            hg_lis.append(hg[i])
        else:
            hg_lis[hg_idx] = hg[i]

    if max_yj < len(yj_lis):
        max_yj = len(yj_lis)
    if max_hg < len(hg_lis):
        max_hg = len(hg_lis)
    yj.rotate()
    hg.rotate()

if max_yj > max_hg:
    print("YJ Win!")
elif max_yj < max_hg:
    print("HG Win!")
else:
    print("Both Win!")