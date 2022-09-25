"""
https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3
"""


def solution(price: int, money: int, count: int):
    diff = ((count*(count+1))/2)*price - money
    if diff <= 0:
        return 0
    else:
        return diff

    
    
from functools import reduce
    
def solution(price: int, money: int, count: int):
    sum = reduce(lambda x, y: x+y, [price*i for i in range(1, count+1)], 0)
    return max(sum-money, 0)