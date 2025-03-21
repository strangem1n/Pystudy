from collections import deque
import math


def solve(n):
    q = deque([])
    summary = 0
    cnt = 0
    prime = next_prime()
    while True:
        if n > summary:
            wait = next(prime)
            if wait > n:
                return cnt
            summary += wait
            q.append(wait)

        else:
            if n == summary:
                cnt += 1
            remove = q.popleft()
            summary -= remove


def next_prime():
    x = 1
    while True:
        x += 1
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                break
        else:
            yield x


N = int(input())
print(solve(N))
