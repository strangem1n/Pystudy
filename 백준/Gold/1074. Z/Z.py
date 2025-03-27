def z(n, cnt, x, y):    # n은 2**n 길이의 정사각형, cnt는 방문 순서
    if n == 1:
        if x == r:
            if y == c:
                return cnt    # (x, y) == (r, c)
            else:
                return cnt+1    # (x, y+1) == (r, c)
        else:
            if y == c:
                return cnt+2    # (x+1, y) == (r, c)
            else:
                return cnt+3    # (x+1, y+1) == (r, c)

    else:    # 영역을 4개로 쪼개 원하는 r, c가 포함된 곳만 골라서 재귀 탐색
        if x <= r < x+2**(n-1) and y <= c < y+2**(n-1):    # 왼쪽 위
            return z(n-1, cnt, x, y)
        elif x <= r < x+2**(n-1) and y+2**(n-1) <= c < y+2**n:    # 오른쪽 위
            return z(n-1, cnt+4**(n-1), x, y+2**(n-1))
        elif x+2**(n-1) <= r < x+2**n and y <= c < y+2**(n-1):    # 왼쪽 아래
            return z(n-1, cnt+2*(4**(n-1)), x+(2**(n-1)), y)
        else:    # 오른쪽 아래
            return z(n-1, cnt+3*(4**(n-1)), x+(2**(n-1)), y+(2**(n-1)))
        

n, r, c = map(int, input().split())
print(z(n, 0, 0, 0))
