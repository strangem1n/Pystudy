import sys
input = sys.stdin.readline

def make_word(string):
    if len(string) == limit:
        if string == S:
            return 1
        else:
            return 0
        
    else:
        if string[0] == 'B' and string[-1] == 'A':
            return max(make_word(string[:0:-1]), make_word(string[:-1]))
        elif string[-1] == 'A':
            return make_word(string[:-1])
        elif string[0] == 'B':
            return make_word(string[:0:-1])
        else:
            return 0

S = input().rstrip()
T = input().rstrip()
limit = len(S)
print(make_word(T))
