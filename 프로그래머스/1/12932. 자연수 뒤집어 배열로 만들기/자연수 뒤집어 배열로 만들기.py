def solution(n):
    slist = list(str(n))
    for i in range(0,len(slist)):
        slist[i] = int(slist[i])
    slist.reverse()
    return slist