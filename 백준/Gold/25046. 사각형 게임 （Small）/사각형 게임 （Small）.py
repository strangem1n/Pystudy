import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
t = 2 ** n
answer = -(float('inf'))

for m in range(t):
    minwoo = str(bin(m))[2:]
    minwoo = "0" * (n - len(minwoo)) + minwoo
    jongjin_best = float('inf')

    for j in range(t):
        jongjin = str(bin(j))[2:]
        jongjin = "0" * (n - len(jongjin)) + jongjin

        score = 0
        temp = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if int(minwoo[r]) + int(jongjin[c]) == 1:
                    score += arr[r][c]
                    temp[r][c] += 1
        if jongjin_best > score:
            jongjin_best = score

    if answer < jongjin_best:
        answer = jongjin_best

print(answer)
