import sys
input = sys.stdin.readline

n = int(input())
arr_a = map(int, input().split())
dict_a = {}
for a in arr_a:
    if dict_a.get(a):
        dict_a[a] += 1
    else:
        dict_a[a] = 1

arr_b = map(int, input().split())
dict_b = {}
for b in arr_b:
    if dict_b.get(b):
        dict_b[b] += 1
    else:
        dict_b[b] = 1

result = 0
result_a = [0] * n
result_b = [0] * n
idx = 0
for num in dict_a:
    if dict_b.get(num):
        share = min(dict_a[num], dict_b[num])
        result += share
        dict_a[num] -= share
        dict_b[num] -= share
        for _ in range(share):
            result_a[idx] = result_b[idx] = num
            idx += 1

a_idx = b_idx = idx
for rest_a, cnt in dict_a.items():
    for _ in range(cnt):
        result_a[a_idx] = rest_a
        a_idx += 1

for rest_b, cnt in dict_b.items():
    for _ in range(cnt):
        result_b[b_idx] = rest_b
        b_idx += 1

print(result)
print(*result_a)
print(*result_b)
