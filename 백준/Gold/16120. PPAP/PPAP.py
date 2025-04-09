word = input()
stack = [None] * len(word)
i = 0
top = -1

while i < len(word):
    top += 1
    stack[top] = word[i]
    if top > 2:
        if stack[top] == stack[top-2] == stack[top-3] == 'P' and stack[top-1] == 'A':
            top -= 3
    i += 1

if top == 0 and stack[top] == 'P':
    print('PPAP')
else:
    print('NP')
