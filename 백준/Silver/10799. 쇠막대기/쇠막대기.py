stack = [0] * 100000
top = -1

iron = input()
result = 0
for i in range(len(iron)):
    if iron[i] == '(':
        top += 1
        stack[top] = 1
    else:
        if stack[top] == 1:
            result += top
        else:
            result += 1
        top -= 1
        stack[top] = 0
print(result)