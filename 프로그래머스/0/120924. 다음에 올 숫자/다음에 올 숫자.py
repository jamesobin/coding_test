def solution(common):
    if (common[1] - common[0]) == (common[2] - common[1]):
        common.append(common[-1] + common[1] - common[0])
    else:
        common.append(common[-1] * (common[1] / common[0]))
    answer = common[-1]
    return answer