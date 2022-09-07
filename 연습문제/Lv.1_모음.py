"""
https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""

def solution(n):
    return sum([int(i) for i in str(n)])

# map 아이디어
def solution(n):
    return sum(map(int, str(n)))

# 재귀 아이디어
def solution(n):
    if n >= 10:
        r = n % 10
        return r + solution(n // 10)
    return n


"""
https://school.programmers.co.kr/learn/courses/30/lessons/12944
"""

def solution(n):
    return [int(i) for i in list(str(n)[::-1])]