import sys
input = sys.stdin.readline

def password(cnt, prev, vow, con):
    if vow == 0 and con == l:
        return
    if vow == l-1 and con == 0:
        return

    if cnt == l:
        if con < 2:
            return
        print(''.join(map(lambda x: chr(x+97), word)))

    else:
        for i in range(prev+1, c):
            if used[i] == 0:
                used[i] = 1
                word[cnt] = arr[i]
                if arr[i] in vowel:
                    password(cnt+1, i, vow+1, con)
                else:
                    password(cnt+1, i, vow, con+1)
                word[cnt] = 0
                used[i] = 0

l, c = map(int, input().split())
arr = list(map(lambda x: ord(x)-97, input().split()))
arr.sort()

vowel = [0, 4, 8, 14, 20]
used = [0] * c
word = [0] * l
password(0, -1, 0, 0)
