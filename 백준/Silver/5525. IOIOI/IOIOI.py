n = int(input())
m = int(input())
string = input().rstrip() + "E"

ioi = 0
ioi_length = 2*n+1
subset = 0
result = 0
for i in range(m+1):
    if ioi != 2 and string[i] == "I":
        if subset >= ioi_length:
            result += (subset - ioi_length) // 2 + 1
        ioi = 1
        subset = 1
    elif ioi == 1 and string[i] == "O":
        ioi = 2
        subset += 1
    elif ioi == 2 and string[i] == "I":
        ioi = 1
        subset += 1
    else:
        if subset >= ioi_length:
            result += (subset - ioi_length) // 2 + 1
        ioi = 0
        subset = 0
print(result)