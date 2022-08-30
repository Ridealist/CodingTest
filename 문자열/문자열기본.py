"""
https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3
"""

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False


def solution(s):
    #함수를 완성하세요
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


def solution(s):
    return s.isdigit() and len(s) in (4, 6)


def alpha_string46(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 


"""
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
"""