import sys
input = sys.stdin.readline

def mix(cnt, prev):
    if cnt > 7:
        return
    else:
        if cnt > 1:
            chk(cnt)

        for i in range(prev+1, n):
            r, g, b = arr[i]
            current[0] += r
            current[1] += g
            current[2] += b
            mix(cnt+1, i)
            current[0] -= r
            current[1] -= g
            current[2] -= b

def chk(cnt):
    global min_diff
    ri = current[0] // cnt
    gi = current[1] // cnt
    bi = current[2] // cnt

    diff = abs(goal[0] - ri) + abs(goal[1] - gi) + abs(goal[2] - bi)
    if min_diff > diff:
        min_diff = diff

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
current = [0, 0, 0]
goal = list(map(int, input().split()))
min_diff = 256 * 3
mix(0, -1)
print(min_diff)