"""
https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3
"""

def solution(d, budget):
    d.sort()
    cnt = 0
    # while len(d) > 0 and d:
    """
    >>> a = [1,2] 
    >>> b = []
    >>> a
    [1, 2]
    >>> bool(a)
    True
    >>> bool(b)
    False
    """
    while len(d) > 0 and budget >= d[0]:
        poped = d.pop(0)
        # if budget < poped:
        #     break
        # else:
        budget -= poped
        cnt += 1

    return cnt


def solution(d, budget):
    d.sort()
    cnt = 0
    while budget > 0 and len(d) > 0:
        poped = d.pop(0)
        if budget < poped:
            break
        else:
            budget -= poped
            cnt += 1

    return cnt