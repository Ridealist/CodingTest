"""
https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=python3
"""

# def solution(arr:list, divisor:int):
#     answer = [i for i in sorted(arr) if i%divisor == 0]
#     if answer:
#         return answer
#     else:
#         return [-1]

def solution(arr:list, divisor:int):
    return [i for i in sorted(arr) if i%divisor == 0] or [-1]

# return a or b : 앞의 것(a)이 false이면 뒤에것(b) 반환