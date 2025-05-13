def chk(num):
    if num % 10 in broken_buttons:
        return False
    else:
        if num < 10:
            return True
        else:
            return chk(num // 10)

n = int(input())
m = int(input())
if m > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

not_use = abs(n - 100)
plus_use = minus_use = float('inf')

if not_use > 0:
    for plus in range(n, 1000001):
        if chk(plus):
            plus_use = plus - n + len(str(plus))
            break

    for minus in range(n, -1, -1):
        if chk(minus):
            minus_use = n - minus + len(str(minus))
            break

print(min(not_use, plus_use, minus_use))
