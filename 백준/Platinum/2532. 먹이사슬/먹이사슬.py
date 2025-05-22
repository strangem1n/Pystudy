import sys
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
animals = set()
for _ in range(n):
    num, l, r = map(int, input().split())
    animals.add((l, r))
animals = list(animals)
animals.sort(key=lambda x: (-x[0], x[1]))

lis = [animals[0][1]]
for i in range(1, len(animals)):
    if lis[-1] <= animals[i][1]:
        lis.append(animals[i][1])
    else:
        idx = bisect_right(lis, animals[i][1])
        lis[idx] = animals[i][1]
print(len(lis))