def solution(emergency):
    desc = sorted(emergency, reverse = True)
    answer = []
    
    for i in range(0, len(emergency)):
        for j in range(0, len(desc)):
            if emergency[i] == desc[j]:
                answer.append(j+1)
    return answer