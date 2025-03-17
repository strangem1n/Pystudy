n = int(input())
grade = input() + "0"
arr = [None] * n
i = 0
idx = 0
while idx < n:
    if grade[i] == "A" or grade[i] == "B" or grade[i] == "C":
        char = grade[i]
        i += 1
        if grade[i] == "+" or grade[i] == "0" or grade[i] == "-":
            arr[idx] = char + grade[i]
            i += 1
            idx += 1
        else:
            arr[idx] = char + "0"
            idx += 1

previous = None
for i in range(n):
    if arr[i] == "A+":
        print("E", end="")
    elif arr[i] == "A0":
        if previous is None or previous == "A-" or previous[0] == "B" or previous[0] == "C":
            print("E", end="")
        else:
            print("P", end="")
    elif arr[i][0] == "C":
        print("B", end="")
    elif arr[i] == "B0" or arr[i] == "B-":
        if previous is None or previous[0] == "C":
            print("D", end="")
        else:
            print("B", end="")
    else:
        if previous is None or previous[0] == "C" or previous == "B-" or previous == "B0":
            print("P", end="")
        else:
            print("D", end="")
    previous = arr[i]
