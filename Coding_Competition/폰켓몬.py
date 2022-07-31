"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    answer = 0
    pick_cnt = int(len(nums) / 2)
    num_set = set(nums)
    num_set_cnt = len(num_set)

    if pick_cnt >= num_set_cnt:
        answer = num_set_cnt
    else:
        answer = pick_cnt

    return answer


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
