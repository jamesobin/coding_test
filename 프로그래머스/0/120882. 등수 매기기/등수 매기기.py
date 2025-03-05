def solution(score):
    avg_list = []
    answer = []
    
    for i in range(0, len(score)):
        avg = (score[i][0] + score[i][1]) / 2
        avg_list.append(avg)
    
    for j in range(0, len(avg_list)):
        rank = 1
        for k in range(0, len(avg_list)):
            if avg_list[j] < avg_list[k]:
                rank += 1
        answer.append(rank)
        
    return answer