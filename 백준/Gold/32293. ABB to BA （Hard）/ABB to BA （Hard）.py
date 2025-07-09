import sys
input = sys.stdin.readline

def solve(word):
    stack = []
    for w in word:
        stack.append(w)
        a = 0
        while len(stack) > 2:
            if stack[-3] == 'A' and stack[-2] == stack[-1] == 'B':
                a += 1
                for _ in range(3):
                    stack.pop()
                stack.append('B')
            else:
                break
        for _ in range(a):
            stack.append('A')
    return ''.join(stack)

t = int(input())
for _ in range(t):
    n = int(input())
    abb = input().rstrip()
    print(solve(abb))
