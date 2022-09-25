"""
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""


def solution(sizes):
    w, h = 0, 0
    for size in sizes:
        w = max(max(w, h), max(size[0], size[1]))
        h = max(min(w, h), min(size[0], size[1]))
    answer = w * h
    return answer


def solution(sizes):
    w = []
    h = []
    for size in sizes:
        size.sort()
        w.append(size[0])
        h.append(size[1])
    return max(w) * max(h)


## zip 함수
## "*" 사용하면 transpose된 배열을 반환하여 zip 시킴
"""
           [
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40]
    ]
"""


def solution(sizes):
    for s in sizes:
        s.sort()
    answer = 1
    for i in zip(*sizes):
        answer *= max(i)
    return answer
