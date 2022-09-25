"""https://programmers.co.kr/learn/courses/30/lessons/42586"""

import math


def howday(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)
    return days


def solution(progresses, speeds):
    days = howday(progresses, speeds)
    answer = []
    count = 0
    std = days[0]
    for i in range(len(days)):
        if days[i] <= std:
            count += 1
        if days[i] > std:
            answer.append(count)
            count = 1
            std = days[i]
        if i == len(days) - 1:
            answer.append(count)
    return answer