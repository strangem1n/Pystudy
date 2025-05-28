import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
pq = list(map(lambda x: -int(x), input().split()))
children = list(map(int, input().split()))

heapq.heapify(pq)

for i in range(m):
    want = children[i]
    present = -heapq.heappop(pq)
    if want > present:
        print(0)
        break
    else:
        present -= want
        heapq.heappush(pq, -present)
else:
    print(1)
