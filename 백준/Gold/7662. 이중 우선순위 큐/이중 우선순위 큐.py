import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    length = 0
    k = int(input())
    used = [0] * k
    for i in range(k):
        order, num = input().rstrip().split()
        num = int(num)
        if order == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            used[i] = 1
            length += 1
        else:
            if length == 0:
                continue
            if num == -1:
                while length > 0:
                    length -= 1
                    num, idx = heapq.heappop(min_heap)
                    if used[idx] == 1:
                        used[idx] = 0
                        break
                    length += 1
            else:
                while length > 0:
                    length -= 1
                    num, idx = heapq.heappop(max_heap)
                    if used[idx] == 1:
                        used[idx] = 0
                        break
                    length += 1

    if length == 0:
        print('EMPTY')
    else:
        max_num, idx = max_heap[0]
        while used[idx] == 0:
            heapq.heappop(max_heap)
            max_num, idx = max_heap[0]

        min_num, idx = min_heap[0]
        while used[idx] == 0:
            heapq.heappop(min_heap)
            min_num, idx = min_heap[0]

        print(-max_num, min_num)
