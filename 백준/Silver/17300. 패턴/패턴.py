def update(num):
    if num == 5:
        not_valid[1].remove(9)
        not_valid[2].remove(8)
        not_valid[3].remove(7)
        not_valid[4].remove(6)
        not_valid[9].remove(1)
        not_valid[8].remove(2)
        not_valid[7].remove(3)
        not_valid[6].remove(4)
    elif num == 2:
        not_valid[1].remove(3)
        not_valid[3].remove(1)
    elif num == 8:
        not_valid[7].remove(9)
        not_valid[9].remove(7)
    elif num == 4:
        not_valid[1].remove(7)
        not_valid[7].remove(1)
    elif num == 6:
        not_valid[3].remove(9)
        not_valid[9].remove(3)


n = int(input())
pattern = list(map(int, input().split()))
not_valid = {
    1: [3, 9, 7],
    2: [8],
    3: [1, 7, 9],
    4: [6],
    5: [],
    6: [4],
    7: [1, 3, 9],
    8: [2],
    9: [1, 3, 7]
}

used = [0] * 10
start = pattern[0]
used[start] = 1
for i in range(1, n):
    update(start)
    end = pattern[i]
    if used[end] == 1:
        print("NO")
        break
    if end in not_valid[start]:
        print("NO")
        break
    used[end] = 1
    start = end
else:
    print("YES")
