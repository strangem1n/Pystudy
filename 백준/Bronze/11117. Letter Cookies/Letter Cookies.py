import copy


def chk(dict_char, chk_word):
    for k in range(len(chk_word)):
        if dict_char.get(chk_word[k]):
            if dict_char[chk_word[k]] > 0:
                dict_char[chk_word[k]] -= 1
            else:
                return "NO"
        else:
            return "NO"
    return "YES"


T = int(input())
for _ in range(T):
    cookie = input()
    box = {}
    for i in range(len(cookie)):
        if box.get(cookie[i]):
            box[cookie[i]] += 1
        else:
            box[cookie[i]] = 1

    word_num = int(input())
    for __ in range(word_num):
        word = input()
        copy_box = copy.deepcopy(box)
        print(chk(copy_box, word))
