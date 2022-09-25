"""
https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""

# 멀티플 할당이 가장 시간복잡도 좋음 - 0.1초대 (0.1 ms)
def solution(n):
    _cur = 1
    _next = 2
    for i in range(1, n):
        _cur, _next = _next, _cur + _next
    return _cur % 1234567


# 메모이제이션 + 제귀 보통 - 1초대 (1 ms)
import sys
sys.setrecursionlimit(1000000)

memo = {1:1, 2:2}

def solution(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = solution(n-1) + solution(n-2)
    
    return memo[n] % 1234567


# 중복조합 + 팩토리얼 제일 구림 - 50초대 (50ms)
import math

def make_comb(n):
    comb_list = []
    for i in range(0, n+1, 2):
        comb = {}
        comb[1] = n-i
        comb[2] = i//2
        comb_list.append(comb)
    return comb_list

make_comb(5)

def solution(n):
    answer = 0
    comb_list = make_comb(n)
    for comb in comb_list:
        one_cnt = int(comb[1])
        two_cnt = int(comb[2])
        answer += math.factorial(one_cnt + two_cnt) // (math.factorial(one_cnt) * math.factorial(two_cnt))
    return answer % 1234567