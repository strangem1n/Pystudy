import sys, math

n, m = map(int, sys.stdin.readline().split())
arr = {}
limit_power = int(math.sqrt(m))

for i in range(2, limit_power+1):
    num = i ** 2
    j = n // num - 1
    while True:
        j += 1
        chk = num * j
        if chk > m:
            break
        elif chk < n:
            continue
        arr[chk] = True

result = 0
for i in range(n, m+1):
    if arr.get(i):
        continue
    else:
        result += 1
print(result)