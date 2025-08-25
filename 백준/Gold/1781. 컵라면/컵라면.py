import sys, heapq
input = sys.stdin.readline

n = int(input())
homework = [[] for _ in range(n)]
for _ in range(n):
    deadline, ramen = map(int, input().split())
    heapq.heappush(homework[deadline-1], -ramen)

result = 0
temp = []
for i in range(n-1, -1, -1):
    while homework[i]:
        left_ramen = heapq.heappop(homework[i])
        heapq.heappush(temp, left_ramen)
    if temp:
        max_ramen = heapq.heappop(temp)
        result -= max_ramen
print(result)