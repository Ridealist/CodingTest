"""
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""

## 풀이 1
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


## 풀이 2
def countdays(progresses, speeds):
    res = []
    for i in range(len(speeds)):
        q, r = divmod((100 - progresses[i]), speeds[i])
        if r == 0:
            res.append(q)
        else:
            res.append(q + 1)
    print(res)
    return res


def solution1(progresses, speeds):
    days = countdays(progresses, speeds)
    answer = []
    while days:
        if days[0] == max(days):
            answer.append(len(days))
            days = []
        cnt = 0
        for i in range(len(days) - 1):
            if days[0] < days[i + 1]:
                cnt += i + 1
                answer.append(cnt)
                days = days[i + 1 :]
                break
    print(answer)
    return answer


def solution1_1(progresses, speeds):
    days = howday(progresses, speeds)
    answer = []
    while days:
        cnt = 0
        for i in range(len(days)):
            if days[0] >= days[i]:
                cnt += 1
                if i == len(days) - 1:
                    answer.append(cnt)
                    days = []
                    break
            if days[0] < days[i]:
                answer.append(cnt)
                days = days[i:]
                break
    print(answer)
    return answer


## 풀이 3
def solution2(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

    if progresses[0] >= 100:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        answer.append(cnt)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

solution(progresses, speeds)
