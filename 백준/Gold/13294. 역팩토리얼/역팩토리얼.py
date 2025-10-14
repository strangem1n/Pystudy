import sys, math
input = sys.stdin.readline

n = input().rstrip()
chk = i = 1
chk_log = math.log10(chk)
l = len(n)
if l < 7:
    n = int(n)
    while chk != n:
        i += 1
        chk *= i
else:
    while math.ceil(chk_log) != l:
        i += 1
        chk_log += math.log10(i)
print(i)
