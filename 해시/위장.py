"""https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3"""


def solution1(clothes):
    dic = {}
    for cloth in clothes:
        try:
            dic[cloth[1]].append(cloth[0])
        except:
            dic[cloth[1]] = [cloth[0]]
    # print(dic)
    answer = 1
    for v in dic.values():
        answer = answer * (len(v) + 1)
    print(answer - 1)
    return answer - 1


def solution2(clothes):
    cloth_type = {}
    for c, t in clothes:
        try:
            cloth_type[t].append(c)
        except:
            cloth_type[t] = [c]
    print(cloth_type)

    cnt = 1
    for n in cloth_type.values():
        cnt = cnt * (len(n) + 1)

    print(cnt - 1)
    return cnt - 1


from collections import Counter
from functools import reduce


def solution3(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: (x + 1) * (y + 1), cnt.values()) - 1
    print(cnt)
    print(answer)
    return answer


clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

solution3(clothes)
