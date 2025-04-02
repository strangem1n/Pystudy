def seat_up_down(t, policy):
    cnt = 0
    set_end = True
    if policy == 0:
        end = 'U'
    elif policy == 1:
        end = 'D'
    elif policy == 2:
        end = t[1]
        set_end = False

    start = t[0]
    for i in range(1, len(t)):
        if start != t[i]:
            cnt += 1
        if set_end and t[i] != end:
            cnt += 1
        else:
            end = t[i]
        start = end

    return cnt


toilet = input()
print(seat_up_down(toilet, 0))
print(seat_up_down(toilet, 1))
print(seat_up_down(toilet, 2))
