import sys
from bisect import bisect_right
input = sys.stdin.readline

n, m = map(int, input().split())
t = int(input())
cats = []
for _ in range(t):
    r, c = map(int, input().split())
    if r > n or c > m:
        continue
    cats.append((r, c))
cats.sort(key=lambda x: (x[0], x[1]))

lis = [cats[0][1]]
for i in range(1, len(cats)):
    if lis[-1] <= cats[i][1]:
        lis.append(cats[i][1])
    else:
        idx = bisect_right(lis, cats[i][1])
        lis[idx] = cats[i][1]
print(len(lis))