exp = input()
stack = []
result = ''

for i in range(len(exp)):
    if exp[i] in ['+', '-']:
        while stack and stack[-1] not in ['+', '-', '(']:
            result += stack.pop()
        if stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(exp[i])
    elif exp[i] in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(exp[i])
    elif exp[i] == '(':
        stack.append(exp[i])
    elif exp[i] == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    else:
        result += exp[i]
while stack:
    result += stack.pop()

print(result)
