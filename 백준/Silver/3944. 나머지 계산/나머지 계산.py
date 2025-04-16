import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    b, d = input().split()
    b = int(b)

    cnt = result = 0
    for i in range(len(d)):
        result += int(d[i]) % (b-1)
        cnt += 1

    print(result % (b-1))
