import sys
input = sys.stdin.readline

def chk():
    stack = ['']
    for k in arr:
        if k == '+':
            stack.append('')
        elif k == '-':
            stack.append('-')
        elif k == ' ':
            continue
        else:
            stack[-1] += k
    result = sum(map(int, stack))
    if result == 0:
        print(''.join(arr))

def f(cnt):
    if cnt == n:
        chk()
    else:
        arr[cnt*2-1] = ' '
        f(cnt+1)
        arr[cnt*2-1] = None
        arr[cnt*2-1] = '+'
        f(cnt+1)
        arr[cnt*2-1] = None
        arr[cnt*2-1] = '-'
        f(cnt+1)
        arr[cnt*2-1] = None

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [None] * (2*n-1)
    for i in range(n):
        arr[i*2] = str(i+1)
    f(1)
    print('')