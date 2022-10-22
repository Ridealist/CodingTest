"""
https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""

def solution(s):
    answer = []
    strip_s = s[2:-2]
    l = strip_s.split("},{")
    l.sort(key=len)
    # print(l)
    for i in l:
        num_l = i.split(",")
        for j in num_l:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


import re
from collections import Counter

def solution(s):
    answer = []
    s = Counter(re.findall('\d+', s))
    tuple_list = s.most_common()
    for i in tuple_list:
        answer.append(int(i[0]))
    return answer


### 프로그래머서 다른 사람 풀이

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

"""
>>> s_c
Counter({'34': 2, '390': 1})
>>> s_c.items()
dict_items([('34', 2), ('390', 1)])
"""