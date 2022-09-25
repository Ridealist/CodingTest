"""
https://school.programmers.co.kr/learn/courses/30/lessons/12919?language=python3
"""

"""
출력 문법!

1. f"abc{val}efg"
2. "abc {} dfg".format()
3. "abc %d cdf" %seoul.index('Kim')

"""

def solution(seoul):
    idx = seoul.index("Kim")
    return f"김서방은 {idx}에 있다"


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


def solution(seoul):
    answer = ''
    return ('김서방은 %d에 있다' %seoul.index('Kim'))