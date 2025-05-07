import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())
sweet = list(map(int, input().split()))
salt = list(map(int, input().split()))
sense = list(map(int, input().split()))

subset = permutations([i for i in range(n)])
max_yummy = -1
for s in subset:
    yummy = 0
    for i in range(1, n):
        if sense[s[i]] * sense[s[i-1]] > k:
            break
        yummy += salt[s[i]] * sweet[s[i-1]]
    else:
        if max_yummy < yummy:
            max_yummy = yummy
print(max_yummy)
