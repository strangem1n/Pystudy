import sys
input = sys.stdin.readline

n = int(input())
classroom = {}
for _ in range(n):
    si, ti = map(int, input().split())
    if classroom.get(si):
        classroom[si] += 1
    else:
        classroom[si] = 1
    if classroom.get(ti):
        classroom[ti] -= 1
    else:
        classroom[ti] = -1

use = list(classroom.items())
use.sort()

max_result = result = 0
for _, room in use:
    result += room
    if max_result < result:
        max_result = result
print(max_result)
