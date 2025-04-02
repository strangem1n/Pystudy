T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
for _ in range(T):
    sentence = input().split()
    for i in range(len(sentence)):
        if sentence[i][0] in vowel:
            sentence[i] += 'yay'
        else:
            idx = 1
            while idx < len(sentence[i]):
                if sentence[i][idx] in vowel:
                    break
                idx += 1
            sentence[i] = sentence[i][idx:] + sentence[i][:idx] + 'ay'
    print(*sentence)
