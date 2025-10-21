import sys
input = sys.stdin.readline

d = [1] * 1000001
for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        d[j] += i
d[0] = 0
for i in range(2, 1000001):
    d[i] += d[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
