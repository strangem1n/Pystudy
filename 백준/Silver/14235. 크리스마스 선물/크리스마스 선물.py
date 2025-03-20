import sys, heapq
input = sys.stdin.readline


# heapq는 기본적으로 최소 힙만 지원하기 때문에 선물의 부호를 바꿔서 음수로 저장
# 절댓값이 클수록 최솟값이 되어 뽑아낸 후 다시 부호를 바꾸면 결과적으로 최댓값이 됨.
n = int(input())
present = []
present_num = 0
for _ in range(n):
    visit = list(map(int, input().split()))
    if visit[0] == 0:
        if present_num < 1:
            print(-1)
        else:
            present_num -= 1
            print(-heapq.heappop(present))
    else:
        present_num += visit[0]
        for i in range(1, visit[0]+1):
            heapq.heappush(present, -visit[i])

