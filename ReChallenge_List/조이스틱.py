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


def findpath(idx, map):
    p_cnt = 0
    m_cnt = 0
    for i in range(len(map)):
        if map[idx + i] == 1:
            p_cnt = i
            break
    for j in range(len(map)):
        if map[idx - j] == 1:
            m_cnt = j
            break
    if p_cnt <= m_cnt:
        n_idx = idx + p_cnt
        map[n_idx] = 0
        return n_idx, map, p_cnt
    else:
        n_idx = idx - m_cnt
        map[n_idx] = 0
        return n_idx, map, m_cnt


m = [0, 0, 1]
i = 0

print(findpath(i, m))


def rightleft(name):
    total = 0
    m = [0]
    for i in name[1:]:
        if i == "A":
            m.append(0)
        else:
            m.append(1)
    i = 0
    while sum(m) > 0:
        n_idx, n_map, cnt = findpath(i, m)
        i = n_idx
        m = n_map
        total += cnt
    
    return total


print(rightleft("JAN"))


def solution(name):
    rl_cnt = rightleft(name)
    ud_cnt = 0
    for i in name:
        ud_cnt += updown(i)

    return rl_cnt + ud_cnt

print(solution("JAN"))