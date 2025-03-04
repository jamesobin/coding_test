def solution(before, after):
    blist = []
    alist = []
    
    for i in range(0, len(before)):
        blist.append(before[i])
        blist.sort()
        alist.append(after[i])
        alist.sort()
    
    if blist == alist:
        answer = 1
    else:
        answer = 0
        
    return answer
