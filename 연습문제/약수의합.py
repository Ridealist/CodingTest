"""
https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
"""
"""
간단한 제곱근은 n**(1/2)로 계산!

시간 복잡도 고려하여 최대한 덜 looping 돌도록!

"""

def solution(n):
    return sum([i for i in range(1,n+1) if n%i==0])


def solution(n):
    return n + sum([i for i in range(1, n//2+1) if n%i==0])


def solution(n):
    left = [i for i in range(1, int(n**(1/2))+1) if n%i==0]
    sqrt = n**(1/2)
    right = [n//i for i in left]
    print(left)
    print(sqrt)
    print(right)
    if sqrt != 0 and n % sqrt == 0:
        return sum(left) + sum(right) - sqrt
    else:
        return sum(left) + sum(right)


import math

def solution(n):
    l = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    print(l)
    return sum(l)