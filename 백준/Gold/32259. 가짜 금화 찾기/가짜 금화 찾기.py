import sys
input = sys.stdin.readline

def question(s, m, e):
    arr = ["?"]
    for i in range(s, m):
        arr.append(i)
    arr.append(0)
    for i in range(m, e):
        arr.append(i)
    arr.append(0)
    print(*arr, flush=True)
    return

n = int(input())
start = 1
end = n
unit = (end - start + 1) // 3

while unit != 0:
    mid_f = start + unit
    mid_s = mid_f + unit
    question(start, mid_f, mid_s)
    ans = input().rstrip()
    if ans == "<":
        if mid_f - start == 1:
            print(f"! {start}", flush=True)
            break
        else:
            end = mid_f
    elif ans == ">":
        if mid_s - mid_f == 1:
            print(f"! {mid_f}", flush=True)
            break
        else:
            start = mid_f
            end = mid_s
    else:
        start = mid_s
    unit = (end - start + 1) // 3

if start == end:
    print(f"! {start}", flush=True)
elif end - start == 1:
    print(f"? {start} 0 {end} 0", flush=True)
    ans = input().rstrip()
    if ans == "<":
        print(f"! {start}", flush=True)
    elif ans == ">":
        print(f"! {end}", flush=True)
