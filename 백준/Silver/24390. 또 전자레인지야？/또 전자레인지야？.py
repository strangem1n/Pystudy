m, s = map(int, input().split(':'))
s += m * 60

timer = button = 0
started = False
while s > timer or not started:
    if (s - timer) >= 600:
        timer += 600
        button += 1
        continue

    if (s - timer) >= 60:
        timer += 60
        button += 1
        continue

    if (s - timer) >= 30:
        timer += 30
        button += 1
        started = True
        continue

    if (s - timer) >= 10:
        timer += 10
        button += 1
        continue

    if s == timer:
        button += 1
        started = True

print(button)