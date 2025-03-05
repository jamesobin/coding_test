def solution(s):
    slist = s.split(" ")
    answer = int(slist[0])
    
    for i in range(1, len(slist)):
        if slist[i] != "Z":
            answer += int(slist[i])
        else:
            answer -= int(slist[i-1])
            
    return answer