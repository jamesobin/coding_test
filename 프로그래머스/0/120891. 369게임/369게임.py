def solution(order):
    order = str(order)
    count = order.count("3") + order.count("6") + order.count("9")
    answer = count
    return answer