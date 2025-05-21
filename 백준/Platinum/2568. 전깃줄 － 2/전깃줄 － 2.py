import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
elec = [tuple(map(int, input().split())) for _ in range(n)]
elec.sort()

lis = [elec[0][1]]
record = [0] * n
for i in range(1, n):
    if elec[i][1] >= lis[-1]:
        lis.append(elec[i][1])
        record[i] = len(lis) - 1
    else:
        idx = bisect_left(lis, elec[i][1])
        lis[idx] = elec[i][1]
        record[i] = idx

remove_elec = []
backtrack = len(lis) - 1
idx = n - 1
while idx > -1:
    if record[idx] == backtrack:
        backtrack -= 1
    else:
        remove_elec.append(elec[idx][0])
    idx -= 1

print(len(remove_elec))
for i in range(len(remove_elec)-1, -1, -1):
    print(remove_elec[i])
