con = ['a', 'i', 'y', 'e', 'o', 'u']
vow = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']


def find_rot13(char, kind):
    if kind == 1:
        char = char.lower()

    for k in range(6):
        if con[k] == char:
            if kind == 1:
                return con[(k+3) % 6].upper()
            return con[(k+3) % 6]

    for k in range(20):
        if vow[k] == char:
            if kind == 1:
                return vow[(k+10) % 20].upper()
            return vow[(k+10) % 20]


while True:
    try:
        word = input()
        for i in range(len(word)):
            if 65 <= ord(word[i]) <= 90:
                print(find_rot13(word[i], 1), end='')
            elif 97 <= ord(word[i]) <= 122:
                print(find_rot13(word[i], 0), end='')
            else:
                print(word[i], end='')
        print('')
    except EOFError:
        break
