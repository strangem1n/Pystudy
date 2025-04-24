import sys
input = sys.stdin.readline

n = int(input())
bank = {}
for _ in range(n):
    x, t, c = map(int, input().split())
    if bank.get(t-x):
        bank[t-x] += c
    else:
        bank[t-x] = c
bank = list(bank.items())
bank.sort(key=lambda k: k[1])
print(bank[-1][1])
