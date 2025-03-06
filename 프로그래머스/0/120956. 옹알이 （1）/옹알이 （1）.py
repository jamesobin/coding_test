def solution(babbling):
    slist = ["aya", "ye", "woo", "ma"]
    
    for i in range(0, len(babbling)):
        for j in range(0, len(slist)):
            babbling[i] = babbling[i].replace(slist[j], " ")
        
        babbling[i] = babbling[i].replace(" ", "")
        
    answer = babbling.count("")
    
    return answer