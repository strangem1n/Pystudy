from collections import deque


def d(n, order):
    ans = (n * 2) % 10000
    return ans, order + 'D'


def s(n, order):
    ans = n - 1
    if ans == -1:
        ans = 9999
    return ans, order + 'S'


def l(n, order):
    ans = (n % 1000) * 10 + n // 1000
    return ans, order + 'L'


def r(n, order):
    ans = (n % 10) * 1000 + n // 10
    return ans, order + 'R'


def result(start, end):
    q = deque([(start, '')])
    while q:
        num, name = q.popleft()
        used[num] = True

        d_num, d_name = d(num, name)
        if d_num == end:
            return d_name
        if not used[d_num]:
            used[d_num] = True
            q.append((d_num, d_name))

        s_num, s_name = s(num, name)
        if s_num == end:
            return s_name
        if not used[s_num]:
            used[s_num] = True
            q.append((s_num, s_name))

        l_num, l_name = l(num, name)
        if l_num == end:
            return l_name
        if not used[l_num]:
            used[l_num] = True
            q.append((l_num, l_name))

        r_num, r_name = r(num, name)
        if r_num == end:
            return r_name
        if not used[r_num]:
            used[r_num] = True
            q.append((r_num, r_name))


T = int(input())
for _ in range(T):
    init, last = map(int, input().split())
    used = [False] * 10000
    print(result(init, last))
