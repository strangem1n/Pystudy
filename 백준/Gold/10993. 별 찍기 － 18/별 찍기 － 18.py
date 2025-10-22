import sys
def star(n, arr):
    if n == 1:
        for a in arr:
            for s in a:
                print(s, end="")
            print("")
        return

    a = len(arr[0])
    b = len(arr[-1])

    if a > b:
        max_len = a * 2 + 3
        arr_top = []
        arr_top.append(" " * (max_len//2) + "*")
        for i in range(1, len(arr)):
            arr_top.append(" " * (max_len//2-i) + "*" + " " * (i*2-1) + "*")
        for i in range(len(arr)):
            arr[i] = " " * (len(arr)-i) + "*" + " " * i + arr[i] + " " * (i*2) + "*"
        new_arr = arr_top + arr + ["*" * max_len]
        star(n-1, new_arr)

    else:
        max_len = b * 2 + 3
        for i in range(len(arr)):
            arr[i] = " " * (i+1) + "*" + " " * (len(arr) - (i+1)) + arr[i] + " " * ((len(arr) - (i+1)) * 2) + "*"
        new_arr = ["*" * max_len] + arr
        for i in range(len(arr)+1, len(arr)*2):
            new_arr.append(" " * i + "*" + " " * ((max_len//2 - i) * 2 - 1) + "*")
        new_arr.append(" " * (max_len//2) + "*")
        star(n-1, new_arr)

num = int(sys.stdin.readline())
star(num, ["*"])