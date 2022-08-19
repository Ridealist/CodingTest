"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
"""


def solution(arr):
    answer = []
    temp = arr[0]
    for idx, val in enumerate(arr):
        if val == temp:
            continue
        else:
            answer.append(temp)
            temp = arr[idx]
    return answer + [arr[-1]]


def solution(arr):
    answer = []
    temp = None
    while arr:
        a = arr.pop(0)
        if a == temp:
            pass
        else:
            temp = a
            answer.append(temp)
    return answer


def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


def solution(arr):
    # 함수를 완성하세요
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i + 1 : i + 2]]


def solution(arr):
    answer = []
    for i in range(len(arr)):
        if [arr[i]] != arr[i + 1 : i + 2]:
            print(arr[i], arr[i + 1 : i + 2])
            answer.append(arr[i])
    return answer
