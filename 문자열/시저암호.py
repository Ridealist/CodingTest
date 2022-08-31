"""
https://school.programmers.co.kr/learn/courses/30/lessons/12926?language=python3
"""


def solution(s, n):
    list_s = list(s)
    lower = {i for i in range(97, 123)}
    upper = {i for i in range(65, 91)}
    
    result = []
    for alpha in list_s:
        if ord(alpha) in lower:
            new_ord = ord(alpha) + n
            if new_ord > 122:
                new_ord = 97 + (new_ord - 123)
            result.append(chr(new_ord))
        elif ord(alpha) in upper:
            new_ord = ord(alpha) + n
            if new_ord > 91:
                new_ord = 91 + (new_ord - 92)
            result.append(chr(new_ord))
        else:
            result.append(" ")
            
    return "".join(result)