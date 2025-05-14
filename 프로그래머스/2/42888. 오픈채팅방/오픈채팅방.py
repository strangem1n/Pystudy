def solution(record):
    chat = {}
    answer = []
    for r in record:
        order, *userinfo = r.split()
        if order == 'Enter':
            uid, nickname = userinfo
            chat[uid] = nickname
            answer.append([1, uid])
        elif order == 'Change':
            uid, nickname = userinfo
            chat[uid] = nickname
        else:
            answer.append([0, userinfo[0]])
    
    for i in range(len(answer)):
        status, uid = answer[i]
        if status == 1:
            answer[i] = f"{chat[uid]}님이 들어왔습니다."
        else:
            answer[i] = f"{chat[uid]}님이 나갔습니다."

    return answer