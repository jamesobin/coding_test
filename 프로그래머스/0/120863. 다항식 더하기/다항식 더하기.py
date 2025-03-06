def solution(polynomial):
    polynomial_list = polynomial.split(" ")
    
    a = 0
    b = 0
    xlist = []
    ylist = []
    
    for i in range(0, len(polynomial_list)):
        if "x" in polynomial_list[i]:
            if polynomial_list[i][:-1] == "":
                xlist.append("1")
            else:
                xlist.append(polynomial_list[i][:-1])
        else:
            if polynomial_list[i] != "+": 
                ylist.append(polynomial_list[i])
                
    for i in range(0, len(xlist)):
        a += int(xlist[i])
    for i in range(0, len(ylist)):
        b += int(ylist[i])
        
    answer = ""

    if b != 0 and a != 0:
        if a != 1:
            answer = str(a) + "x + " + str(b)
        else:
            answer = "x + " + str(b)
    elif b == 0 and a != 0:
        if a != 1:
            answer = str(a) + "x"
        else:
            answer = "x"
    else:
        answer = str(b)
        
    return answer