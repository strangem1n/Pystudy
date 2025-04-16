word = input()
cnt = 0
next_word = 'H'

for i in range(len(word)):
    if word[i] == next_word == 'H':
        next_word = 'O'
    elif word[i] == next_word == 'O':
        next_word = 'N'
    elif word[i] == next_word == 'N':
        next_word = 'I'
    elif word[i] == next_word == 'I':
        next_word = 'H'
        cnt += 1

print(cnt)