def solve(num, size):
    sum_box = 0
    cnt = 0
    for i in range(num-1, 0, -1):
        sum_box += box[i]
        cnt += 1
        if box[i-1] - size >= sum_box / cnt or box[i-1] + size <= sum_box / cnt:
            return "unstable"
    return "stable"


n, l = map(int, input().split())
box = list(map(int, input().split()))
print(solve(n, l))
