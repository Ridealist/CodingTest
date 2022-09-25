"""
https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=python3
"""


import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            answer -= i
        else:
            answer += i
    return answer


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i**(1/2) == int(i**(1/2)):
            answer -= i
        else:
            answer += i
    return answer


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer