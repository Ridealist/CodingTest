"""
https://school.programmers.co.kr/learn/courses/30/lessons/62048?language=python3
"""

# 8/22도전 테스트 11만 시간초과로 실패. 94.4/100

def max_pair(w:int, h:int):
    pair = None
    for i in range(2, max(w,h)+1):
        if w%i == 0 and h%i == 0:
            pair = i
    return pair


def solution(w:int, h:int):
    pair = max_pair(w, h)
    if pair:
        w = w//pair
        h = h//pair

    s = 0
    for i in range(w):
        s += (int((h/w)*(i+1)) - int((h/w)*i)) * (w-(i+1))
    
    broke_n = w*h - 2*s

    if pair:
        broke_np = broke_n * pair
        return w*h - broke_np
    
    else:
        return 2*s

def max_pair(w:int, h:int):
    pair = 1
    m = min(w,h)
    for i in range(2, m+1):
        if w%i == 0 and h%i == 0:
            pair = i
            return pair * max_pair(w//i, h//i)
        
    return 1

# print(max_pair(16,24))


## 최종 코드
def max_pair(w:int, h:int):
    pair = 1
    m = min(w,h)
    for i in range(2, m+1):
        if w%i == 0 and h%i == 0:
            pair = i
            return pair * max_pair(w//i, h//i)
    return 1


def solution(w:int, h:int):
    pair = max_pair(w, h)

    w = w//pair
    h = h//pair

    s = sum((int((h/w)*(i+1)) - int((h/w)*i)) * (w-(i+1)) for i in range(w))

    
    # m = min(w,h)
    # M = max(w,h)

    # s = sum((int((M/m)*(i+1)) - int((M/m)*i)) * (m-(i+1)) for i in range(m))
    

    broke_n = w*h - 2*s
    return w*h*pair**2 - broke_n*pair