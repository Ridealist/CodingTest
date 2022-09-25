"""
https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3
"""

# count 함수 문자열내 해당 문자 갯수
# from collections import Counter
# Counter("문자열") -> 문자열 내 빈도수 자동 집계
# ex) >>> from collections import Counter
# >>> c = Counter(a.lower()) 
# >>> Counter({'o': 3, 'p': 2, 'y': 2})


def solution(s):
    s = s.lower()
    s_list = list(s)
    cnt_p = 0
    cnt_y = 0
    for i in s_list:
        if i == "p":
            cnt_p += 1
        elif i == "y":
            cnt_y += 1
    if cnt_p == cnt_y:
        return True
    else:
        return False


def solution(s):
    if s.lower().count("p") == s.lower().count("y"):
        return True
    return False


def solution(s):
    if len(s.lower().split("p")) == len(s.lower().split("y")):
        return True
    return False



from collections import Counter
def numPY(s):
    # 함수를 완성하세요
    c = Counter(s.lower())
    return c['y'] == c['p'] 