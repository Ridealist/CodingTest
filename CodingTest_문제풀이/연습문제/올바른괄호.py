"""
https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
"""

def solution(s):
    
    l = list(s)
    
    stack = []
    for i in l:
        if i == "(":
            stack.append(i)
        else:
            if "(" in stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True