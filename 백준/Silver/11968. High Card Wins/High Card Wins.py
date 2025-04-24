import sys
input = sys.stdin.readline

n = int(input())
elsie = [0] * (2*n+1)
for _ in range(n):
    elsie[int(input())] = 1

i = j = 1
cnt = 0
while True:
    while i < 2*n+1 and elsie[i] == 0:
        i += 1
    while j < 2*n+1 and elsie[j] == 1:
        j += 1

    if i == 2*n+1 or j == 2*n+1:
        break

    if i < j:
        cnt += 1
        i += 1
        j += 1
    else:
        j += 1
print(cnt)
