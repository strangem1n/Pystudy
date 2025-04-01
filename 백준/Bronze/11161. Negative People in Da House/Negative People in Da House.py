T = int(input())
for _ in range(T):
    M = int(input())
    min_result = 0
    result = 0
    for __ in range(M):
        p1, p2 = map(int, input().split())
        result += p1
        result -= p2
        if min_result > result:
            min_result = result
    print(-min_result)
