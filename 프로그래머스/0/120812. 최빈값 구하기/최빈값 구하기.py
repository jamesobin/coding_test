def solution(array):
    count_list = []
    
    for i in range(0, len(array)):
        count = 0
        temp = []
        for j in range(0, len(array)):
            if array[i] == array[j]:
                count += 1
        temp.append(array[i])
        temp.append(count)
        
        if temp not in count_list:
            count_list.append(temp)
    
    max = count_list[0][1]
    answer = array[0]
    
    for i in range(1, len(count_list)):
        if max < count_list[i][1]:
            max = count_list[i][1]
            answer = count_list[i][0]
        elif max == count_list[i][1]:
            answer = -1
            
    return answer