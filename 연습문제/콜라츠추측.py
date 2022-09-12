"""
https://school.programmers.co.kr/learn/courses/30/lessons/12943
"""

cnt = 0

def solution(num):
    global cnt   
    
    while num > 1 and cnt <= 500:
        cnt += 1
        if num%2 == 0:
            num = num//2
            return solution(num)
        else:
            num = num*3 + 1
            return solution(num)
    
    if num == 1:
        return cnt
    else:
        return -1


def solution(num):
    cnt = 0

    while num > 1 and cnt <= 500:
        if num%2 == 0:
            num = num//2
        else:
            num = num*3 + 1
        cnt += 1

    if num == 1:
        return cnt
    else:
        return -1


def solution(num):
    global cnt
    
    if num == 1:
        return cnt if cnt <= 500 else -1

    if num%2 == 0:
        num = num // 2
    else:
        num = num*3 + 1
    cnt += 1
    
    return solution(num)
