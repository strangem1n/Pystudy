T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201    # 복도를 각 200칸으로
    for i in range(N):
        a, b = map(int, input().split())
        if a > b:    # 출발 지점이 도착 지점보다 항상 작게
            a, b = b, a
        if a % 2 == 1:    # 출발점을 짝수로 맞춤
            a += 1
        if b % 2 == 1:    # 도착점도 짝수로 맞춤
            b += 1
        for j in range(a, b+1, 2):    # 출발해서 도착하기까지 거쳐야 하는 복도 칸 인덱스에 +1
            corridor[j//2] += 1
    result = -1
    for i in range(1, 201):
        if result < corridor[i]:    # 가장 많이 거쳐야 하는 복도의 횟수가 곧 걸리는 시간
            result = corridor[i]
    print(f"#{tc} {result}")
