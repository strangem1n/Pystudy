T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    day = (N // C)
    if N % C > 0:
        day += 1
    print(day)