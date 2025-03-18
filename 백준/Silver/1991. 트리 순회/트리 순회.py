def solve(n, start, order):
    for i in range(n):
        if arr[i][0] == start:
            break

    if order == 0:
        print(start, end="")
        if arr[i][2] != ".":
            solve(n, arr[i][2], order)
        if arr[i][4] != ".":
            solve(n, arr[i][4], order)
    elif order == 1:
        if arr[i][2] != ".":
            solve(n, arr[i][2], order)
        print(start, end="")
        if arr[i][4] != ".":
            solve(n, arr[i][4], order)
    else:
        if arr[i][2] != ".":
            solve(n, arr[i][2], order)
        if arr[i][4] != ".":
            solve(n, arr[i][4], order)
        print(start, end="")


n = int(input())
arr = [input() for _ in range(n)]
solve(n, "A", 0)
print("")
solve(n, "A", 1)
print("")
solve(n, "A", 2)
print("")
