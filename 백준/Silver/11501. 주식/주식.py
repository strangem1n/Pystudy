import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    total = 0
    max_price = price[-1]
    stack = []

    for i in range(N-2, -1, -1):
        if price[i] < max_price:
            stack.append(price[i])
        elif price[i] > max_price:
            for s in stack:
                total += max_price - s
            max_price = price[i]
            stack = []

    for s in stack:
        total += max_price - s
        
    print(total)
