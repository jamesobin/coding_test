def solution(id_pw, db):
    for i in range(0, len(db)):
        if id_pw[0] == db[i][0]:
            if id_pw[1] == db[i][1]:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
        
    return answer