"""
https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""

def solution(s):
    s_list = [int(i) for i in s.split(" ")]
    m = str(min(s_list))
    M = str(max(s_list))
    return " ".join([m, M])


## why?/??
def solution(s):
    s_list = list(map(int, s.split(" ")))
    return " ".join([min(s_list), max(s_list)])

print(solution("-1 -2 -3 -4"))