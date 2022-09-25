"""https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3"""


import queue


l1 = [(0, 2), (1, 1), (2, 3), (3, 2)]
l2 = [(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)]


def tuply(l):
    t_l = []
    for idx, val in enumerate(l):
        t = (idx, val)
        t_l.append(t)
    return t_l


def popin(tuple_list, location):
    i = 0
    while len(tuple_list) > 0:
        t = tuple_list.pop(0)
        for idx, prior in tuple_list:
            if t[1] < prior:
                tuple_list.append(t)
                break
        if t not in tuple_list:
            i += 1
            if t[0] == location:
                return i


def solution(priorities, location):
    tuple_list = tuply(priorities)
    answer = popin(tuple_list, location)
    return answer


def solution2(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        t = queue.pop(0)
        if any(t[1] < q[1] for q in queue):
            queue.append(t)
        else:
            answer += 1
            if t[0] == location:
                return answer
