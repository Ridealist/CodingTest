"""
https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=python3
"""

def solution(a, b):
    # weeks = "SUN,MON,TUE,WED,THU,FRI,SAT".split(",")
    # str class의 built-in method들 활용하기!
    # https://www.w3schools.com/python/python_ref_string.asp
    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU",]
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    s = sum(days[:a]) + b - 1
    
    return weeks[s%7]


# https://docs.python.org/ko/3/library/datetime.html
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.date(2016, a, b).weekday()]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))