"""
https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3
"""

import string

upper = string.ascii_uppercase

# 'ABCDEFGHIJKLM' 'N' 'OPQRSTUVWXYZ'

# def solution(name):
#     answer = 0
#     return answer

def updown(alpha: str):
    alpha_dict = {}
    for i, val in enumerate('ABCDEFGHIJKLMN'):
        alpha_dict[val] = i
    for i, val in enumerate('OPQRSTUVWXYZ'):
        alpha_dict[val] = 12-i
    # print(alpha_dict)
    return alpha_dict[alpha]


def rightleft(name):
    nota_cnt = 0
    a_cnt = 0
    isastart = False
    
    for i in name:
        if i != "A" and isastart is True:
            break
        if i != "A":
            nota_cnt += 1
        else:
            a_cnt += 1
            isastart = True
    
    if nota_cnt <= a_cnt:
        return (nota_cnt-1)*2 + len(name) - nota_cnt - a_cnt
    else:
        return len(name) - 1

def solution(name):
    rl_cnt = rightleft(name)
    ud_cnt = 0
    for i in name:
        ud_cnt += updown(i)

    return rl_cnt + ud_cnt