"""
https://school.programmers.co.kr/learn/courses/30/lessons/12924
"""

def solution(n):
    result = 0
    for i in range(1, n+1):
        s = 0
        m = 0
        while s < n:
            s += i + m
            m += 1
        if s == n:
            # print(i, s, m, n)
            result += 1
            
    return result