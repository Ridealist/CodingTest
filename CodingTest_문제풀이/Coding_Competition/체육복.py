"""
https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""


def solution(n, lost, reserve):
    for num in list(reserve):
        if num in lost:
            lost.remove(num)
            reserve.remove(num)

    reserve.sort()
    for num in reserve:
        if num - 1 in lost:
            lost.remove(num - 1)
        elif num + 1 in lost:
            lost.remove(num + 1)

    answer = n - len(lost)
    return answer


"""
참고사항
https://www.educative.io/courses/python-ftw-under-the-hood/Y5KX19qkxrO
"""
