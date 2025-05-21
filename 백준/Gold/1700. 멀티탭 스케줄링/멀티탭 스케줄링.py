n, k = map(int, input().split())
arr = list(map(int, input().split()))

multi_tap = set()
left_hole = n
cnt = 0

for i in range(k):
    a = arr[i]
    if a in multi_tap:
        continue
    elif left_hole > 0:
        left_hole -= 1
        multi_tap.add(a)
    else:
        use_idx = []
        for e in multi_tap:
            for j in range(i+1, k):
                if e == arr[j]:
                    use_idx.append((j, e))
                    break
            else:
                use_idx.append((k, e))
        use_idx.sort()
        multi_tap.remove(use_idx[-1][1])
        multi_tap.add(a)
        cnt += 1
print(cnt)
