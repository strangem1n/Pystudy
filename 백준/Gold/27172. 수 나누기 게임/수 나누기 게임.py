import sys, math
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
divisor = {1: []}
for i in range(n):
    num = cards[i]
    divisor[1].append(i)
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            if divisor.get(j):
                divisor[j].append(i)
            else:
                divisor[j] = [i]
            if num // j != j:
                if divisor.get(num//j):
                    divisor[num//j].append(i)
                else:
                    divisor[num//j] = [i]

result = [0] * n
for i in range(n):
    num = cards[i]
    if divisor.get(num):
        for j in divisor[num]:
            result[j] -= 1
        result[i] += len(divisor[num])

print(*result)
