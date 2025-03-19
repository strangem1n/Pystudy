from collections import deque

T = int(input())
for _ in range(T):
    func = input()
    len_arr = int(input())
    reverse = 0
    arr = deque(input()[1:-1].split(","))
    for i in range(len(func)):
        if func[i] == "R":
            reverse += 1
        else:
            if len_arr <= 0:
                print("error")
                break
            else:
                if reverse % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
                len_arr -= 1
    else:
        if reverse % 2 == 1:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
