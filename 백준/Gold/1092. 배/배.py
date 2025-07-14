import sys
input = sys.stdin.readline

crane = int(input())
c_arr = sorted(map(int, input().split()), reverse=True)
box = int(input())
b_arr = sorted(map(int, input().split()), reverse=True)

cycle = 0
cnt = box
chk = [False] * box

if c_arr[0] < b_arr[0]:
    cycle = -1
else:
    while cnt > 0:
        cycle += 1
        ci = bi = 0
        while bi < box and ci < crane:
            if not chk[bi] and c_arr[ci] >= b_arr[bi]:
                chk[bi] = True
                ci += 1
                cnt -= 1
            bi += 1
print(cycle)
