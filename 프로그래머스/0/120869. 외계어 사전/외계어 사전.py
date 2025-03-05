def solution(spell, dic):
    for i in range(0, len(spell)):
        for j in range(0, len(dic)):
            if spell[i] not in dic[j]:
                dic[j] = ""
    if (len(dic) - dic.count("")) > 0:
        answer = 1
    else:
        answer = 2
    return answer
