def solution(my_string):
    slist = my_string.split(" ")

    num = []
    operator = []
    
    for i in range(0, len(slist)):
        if i % 2 == 0:
            num.append(int(slist[i]))
        else:
            operator.append(slist[i])
            
    answer = num[0]
            
    for i in range(0, len(operator)):
        if operator[i] == "+":
            answer += num[i+1]
        elif operator[i] == "-":
            answer -= num[i+1]
    
    return answer
