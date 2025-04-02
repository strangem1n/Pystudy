T = int(input())
for _ in range(T):
    sentence = input().split()
    result = 0
    for i in range(len(sentence)):
        if sentence[i] == "u" or sentence[i] == "ur":
            result += 10
        elif sentence[i] == "would" or sentence[i] == "should":
            if i < len(sentence)-1 and sentence[i+1] == "of":
                result += 10
        elif len(sentence[i]) > 2:
            for j in range(len(sentence[i])-2):
                if sentence[i][j:j+3] == "lol":
                    result += 10
                    break
    print(result)
