import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
result = [0] * n

stack = []
for i in range(n-1, -1, -1):
    while stack and stack[-1][0] < tower[i]:
        result[stack[-1][1]] = i+1
        stack.pop()
    stack.append((tower[i], i))

print(*result)
