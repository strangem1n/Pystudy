T = int(input())
for _ in range(T):
    test = input().strip()
    try:
        test = int(test)
        if test < 0:
            print('invalid input')
        else:
            print(test)
    except:
        print('invalid input')
