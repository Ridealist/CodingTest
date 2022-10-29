"""
https://school.programmers.co.kr/learn/courses/30/lessons/12911
"""

def tobinary(n):
    b = ''
    while n > 0:
        b += str(n % 2)
        n = n // 2
    return b[::-1]

print(tobinary(100))

def solution(n):
    bin = tobinary(n)
    answer = ''
    if '0' in bin:
        bin.find('0')
    else:
        answer += '10' + bin[1:]
        return int(answer, 2)