import sys
from bisect import bisect_left
input = sys.stdin.readline

def solve(idx):
    increase = arr[:idx+1]
    decrease = dec[idx:]
    inc_ans = [increase[0]]
    dec_ans = [decrease[0]]

    for i in range(1, len(increase)):
        if increase[i] > inc_ans[-1]:
            inc_ans.append(increase[i])
        else:
            pos = bisect_left(inc_ans, increase[i])
            inc_ans[pos] = increase[i]

    for i in range(1, len(decrease)):
        if decrease[i] > dec_ans[-1]:
            dec_ans.append(decrease[i])
        else:
            pos = bisect_left(dec_ans, decrease[i])
            dec_ans[pos] = decrease[i]

    return len(inc_ans) + len(dec_ans) - 1

n = int(input())
arr = list(map(int, input().split()))
dec = list(map(lambda x: -x, arr))

max_length = 0
for k in range(n):
    max_length = max(max_length, solve(k))
print(max_length)
