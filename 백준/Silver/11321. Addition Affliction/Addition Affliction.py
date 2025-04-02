while True:
    exp = input()
    if exp == "0":
        break

    arr = list(map(int, exp.split("+")))
    used = [0] * len(arr)
    pair = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if used[i] == used[j] == 0 and (arr[i] + arr[j]) % 10 == 0:
                used[i] = used[j] = 1
                pair.append([i, j])

    new_arr = [0] * len(arr)
    idx = 0
    while pair:
        i, j = pair.pop()
        new_arr[idx], new_arr[idx+1] = arr[i], arr[j]
        idx += 2

    for i in range(len(arr)):
        if used[i] == 0:
            new_arr[idx] = arr[i]
            idx += 1

    print('+'.join(map(str, new_arr)))
