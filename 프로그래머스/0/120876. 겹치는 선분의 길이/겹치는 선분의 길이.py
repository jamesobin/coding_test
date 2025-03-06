def solution(lines):
    answer = 0
    list1 = lines[0]
    list2 = lines[1]
    list3 = lines[2]
    obj1 = []
    obj2 = []
    obj3 = []
    
    for i in range(list1[0], list1[1] + 1):
        obj1.append(i)
    for i in range(list2[0], list2[1] + 1):
        obj2.append(i)
    for i in range(list3[0], list3[1] + 1):
        obj3.append(i)
    
    line1 = 0
    for i in range(0, len(obj1)):
        for j in range(0, len(obj2)):
            if obj1[i] == obj2[j]:
                line1 += 1
                
    line2 = 0
    for i in range(0, len(obj2)):
        for j in range(0, len(obj3)):
            if obj2[i] == obj3[j]:
                line2 += 1
                
    line3 = 0
    for i in range(0, len(obj3)):
        for j in range(0, len(obj1)):
            if obj3[i] == obj1[j]:
                line3 += 1
                
    line4 = 0
    for i in range(0, len(obj1)):
        for j in range(0, len(obj2)):
            for k in range(0, len(obj3)):
                if obj1[i] == obj2[j] == obj3[k]:
                    line4 += 1
    
    if line1 > 0:
        line1 -= 1
    if line2 > 0:
        line2 -= 1
    if line3 > 0:
        line3 -= 1
    if line4 > 0:
        line4 -= 1
        
    answer = line1 + line2 + line3 - 2 * line4
        
    return answer