n = int(input())
cow = list(map(int, input().split()))

cow.sort(reverse=True)
idx = 0
for i in range(n):
    if cow[i] >= idx:
        idx += 1
    else:
        break
print(idx)
