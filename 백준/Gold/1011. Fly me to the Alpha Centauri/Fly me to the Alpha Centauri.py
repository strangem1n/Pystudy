import sys
input = sys.stdin.readline

def move(num):
    cnt = 0
    chk = 0
    add = 1
    while True:
        if chk < num:
            cnt += 1
            chk += add
        else:
            return cnt
        if chk < num:
            cnt += 1
            chk += add
            add += 1
        else:
            return cnt

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    diff = y - x
    print(move(diff))
