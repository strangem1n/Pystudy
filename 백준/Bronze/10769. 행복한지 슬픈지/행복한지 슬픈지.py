word = input()
happy = sad = 0
for i in range(len(word)-2):
    if word[i] == ':' and word[i+1] == '-' and word[i+2] == ')':
        happy += 1
    elif word[i] == ':' and word[i+1] == '-' and word[i+2] == '(':
        sad += 1

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    if happy == sad == 0:
        print('none')
    else:
        print('unsure')
