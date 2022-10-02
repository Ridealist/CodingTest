def solution(train):
    answer = 0
    
    for i in train:
        answer += i.count("EW")

    r = ["" for _ in range(len(train[0]))]
    for j in train:
        for idx in range(len(train[0])):
            r[idx] += j[idx]
    
    for j in r:
        answer += j.count("SN")
    
    return answer
