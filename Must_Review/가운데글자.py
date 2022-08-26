"""
https://school.programmers.co.kr/learn/courses/30/lessons/12903/solution_groups?language=python3
"""

# 효율화 방안 고민!

def solution(s:str):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2 -1 : len(s)//2 + 1]
