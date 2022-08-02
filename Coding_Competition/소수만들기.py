"""
https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""

### 준보 풀이
import itertools

# 소수 판별 함수
def Prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# index 조합 함수
def Choose(nums):
    n = len(nums)
    total = []
    for j in range(0, n - 2):
        a = []
        a.append(j)
        for i in range(j + 1, n - 1):
            a.append(i)
            for k in range(i + 1, n):
                a.append(k)
                total.append(a)
                a = []
                a.append(j)
                a.append(i)
            a = []
            a.append(j)
    # print(total)
    return total


def solution0(nums):
    answer = 0
    idx_obj = itertools.combinations(range(len(nums)), 3)
    # ex) nums=[1,2,3,4] -> (0,1,2) (0,1,3) ... (1,2,3) 만들어 줌

    for idx in idx_obj:
        num = 0
        for i in idx:
            num += nums[i]

        # 소수 판별
        if Prime(num):
            answer += 1

    print(answer)
    return answer


def solution(nums):
    answer = 0
    coms = itertools.combinations(nums, 3)

    for com in coms:
        if Prime(sum(com)):
            answer += 1

    print(answer)
    return answer


nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 7, 6, 4]

solution(nums1)

### 회택 풀이
from itertools import combinations
from math import sqrt


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_prime(sum(i)):
            answer += 1
    return answer


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
