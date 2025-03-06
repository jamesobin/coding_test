def solution(quiz):
    answer = []
    
    for i in range(0, len(quiz)):
        obj = quiz[i].split(" ")
        
        if obj[1] == "+":
            if (int(obj[0]) + int(obj[2])) == int(obj[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if (int(obj[0]) - int(obj[2])) == int(obj[4]):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer