def solution(s):
    slist = list(s)
    slist.sort()
    answer = ""
    
    for i in range(0, len(slist)):
        if slist.count(slist[i]) == 1:
            answer += slist[i]

    return answer