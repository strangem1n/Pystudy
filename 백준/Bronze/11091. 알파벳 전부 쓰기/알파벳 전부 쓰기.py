def chk_pan(s):
    chk = [1] * 26
    for i in range(len(s)):
        idx = ord(s[i]) - 97
        if 0 <= idx <= 25:
            chk[idx] -= 1

    miss = ''
    for i in range(26):
        if chk[i] > 0:
            miss += chr(i+97)

    if len(miss) > 0:
        return "missing " + miss
    else:
        return "pangram"


T = int(input())
for _ in range(T):
    sentence = input().lower()
    print(chk_pan(sentence))
