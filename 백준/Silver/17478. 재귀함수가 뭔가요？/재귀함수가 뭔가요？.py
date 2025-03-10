def f(n):
    if n == 0:
        sentence1 = '"재귀함수가 뭔가요?"'
        sentence2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
        sentence3 = '라고 답변하였지.'
        ans = [sentence1, sentence2, sentence3]
        return ans

    else:
        sentence1 = '"재귀함수가 뭔가요?"'
        sentence2 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
        sentence3 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
        sentence4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
        ans = [sentence1, sentence2, sentence3, sentence4]
        inner_sentence = f(n-1)
        for s in inner_sentence:
            s = '____' + s
            ans.append(s)
        sentence5 = '라고 답변하였지.'
        ans.append(sentence5)
        return ans

n = int(input())
result = f(n)
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
for sentence in result:
    print(sentence)
