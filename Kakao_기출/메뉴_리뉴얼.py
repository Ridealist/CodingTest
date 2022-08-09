"""
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""

# 준보 풀이
import itertools


def course_combination(orders, course):
    courses = course
    cnt_set_list = []
    for course in courses:
        cnt_set = {}
        for order in orders:
            order_combs = itertools.combinations(order, course)
            for com in order_combs:
                key_list = sorted([com[i] for i in range(len(com))])
                key = ""
                for k in key_list:
                    key += k
                if key in cnt_set:
                    cnt_set[key] += 1
                else:
                    cnt_set[key] = 1
        cnt_set_list.append(cnt_set)
    # print(cnt_set_list)
    return cnt_set_list


def solution(orders, course):
    answer = []
    cnt_set_list = course_combination(orders, course)
    for cnt_set in cnt_set_list:
        m = 2
        m_list = []
        for cnt in cnt_set:
            if cnt_set[cnt] > m:
                m_list = []
                m = cnt_set[cnt]
                m_list.append(cnt)
            elif cnt_set[cnt] == m:
                m_list.append(cnt)
            else:
                continue
        answer += m_list
    return sorted(answer)


# 회택 풀이
from itertools import combinations


def solution(orders, course):
    countCourse = {}

    for c in course:
        c_dict = countCourse.get(c, {})

        for person in orders:
            coms = combinations(person, c)
            for com in coms:
                com = "".join(sorted(com))
                c_dict[com] = c_dict.get(com, 0) + 1
        countCourse[c] = c_dict
    answer = []
    for c in course:
        coms = countCourse[c]
        # print(coms)
        s = sorted(coms, key=lambda x: coms[x], reverse=True)
        # print("s[0]", s[0])
        # print("coms[s[0]]", coms[s[0]])
        if not s:
            continue
        max_count = coms[s[0]]

        if max_count >= 2:
            for i in s:
                if coms[i] == max_count:
                    answer.append(i)
                else:
                    break
    answer.sort()
    return answer


# 승희 풀이
from itertools import combinations


def solution(orders, course):
    sort = [sorted(o) for o in orders]
    result = []

    for num in course:
        cnt = {}
        for s in sort:
            for c in list(combinations(s, num)):
                string = "".join(c)
                cnt[string] = cnt[string] + 1 if string in cnt else 1

        maximum = {}
        for key, value in cnt.items():
            if value > 1 and value in maximum:
                maximum[value].append(key)
            elif value > 1:
                maximum[value] = [key]
        if list(maximum.keys()):
            result += maximum[max(list(maximum.keys()))]
    result.sort()
    return result
