"""
https://school.programmers.co.kr/learn/courses/30/lessons/12922?language=python3
"""

"""
# 제너레이터
https://wikidocs.net/16069

https://twpower.github.io/120-python-in-operator-time-complexity
"""
"""
# itertools

https://docs.python.org/ko/3/library/itertools.html?highlight=cycle
"""

def solution(n):
    l = ["수", "박"]
    cnt = 0
    answer = ''
    while cnt < n:
        cnt += 1
        answer += l[(cnt-1)%2]
    return answer


## generator
def watermellon_gen():
    l = ["수", "박"]
    cnt = -1
    while True:
        cnt += 1
        yield l[cnt%2]

def soution(n):
    answer = ""
    gen = watermellon_gen()
    while n:
        answer += next(gen)
        n -= 1


import itertools

def solution(n):
    answer = ""
    c = itertools.cycle("수박")
    while n:
        answer += next(c)
        n -= 1
    return answer