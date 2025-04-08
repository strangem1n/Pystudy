from collections import deque
import sys
input = sys.stdin.readline

d = deque([])
length = 0
n = int(input())

for _ in range(n):
    order = input().rstrip()
    if order == 'pop_front':
        if length == 0:
            print(-1)
        else:
            print(d.popleft())
            length -= 1
    elif order == 'pop_back':
        if length == 0:
            print(-1)
        else:
            print(d.pop())
            length -= 1
    elif order == 'size':
        print(length)
    elif order == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if length == 0:
            print(-1)
        else:
            print(d[0])
    elif order == 'back':
        if length == 0:
            print(-1)
        else:
            print(d[-1])
    else:
        pp, num = order.split()
        num = int(num)
        if pp == 'push_front':
            d.appendleft(num)
            length += 1
        else:
            d.append(num)
            length += 1
