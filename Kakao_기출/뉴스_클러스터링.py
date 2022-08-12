"""
https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""


def transform(word: str):
    word = word.lower()
    str_list = []
    for i in range(len(word) - 1):
        if word[i : i + 2].isalpha():
            str_list.append(word[i : i + 2])
    # print(str_list)
    return str_list


def jacard(l1: list, l2: list):
    if len(l1 + l2) == 0:
        return 1
    l1_dict = {}
    l2_dict = {}
    for i in l1_dict:
        if i not in l1_dict:
            l1_dict[i] = 1
        else:
            l1_dict[i] += 1
    for i in l2_dict:
        if i not in l2_dict:
            l2_dict[i] = 1
        else:
            l2_dict[i] += 1

    keys = set(l1 + l2)
    inter_n = 0
    union_n = 0
    for key in keys:
        if (key in l1_dict) & (key in l2_dict):
            inter_n += min(l1_dict[key], l2_dict[key])
            union_n += max(l1_dict[key], l2_dict[key])
        elif key in l1_dict:
            union_n += l1_dict[key]
        elif key in l2_dict:
            union_n += l2_dict[key]

    # print(inter_n, union_n)
    return inter_n / union_n


def jacard(l1: list, l2: list):
    if len(l1 + l2) == 0:
        return
    inter_set = set(l1) & set(l2)
    inter_n = 0
    union_n = 0
    for i in inter_set:
        inter_n += min(l1.count(i), l2.count(i))

    for i in inter_set:
        union_n += max(l1.count(i), l2.count(i))


# 회택
def jacard1(l1: list, l2: list):
    if len(l1 + l2) == 0:
        return 1

    inter_set = set(l1) & set(l2)
    inter = []
    for i in inter_set:
        inter.extend([i] * min(l1.count(i), l2.count(i)))
    union = l1 + l2
    for i in inter:
        union.remove(i)

    return len(inter) / len(union)


# 홍동
"""

    const newCombiStr1 = []
    const intersection = combiStr1.filter(item => {
        if(combiStr2.includes(item)) {
            const index = combiStr2.indexOf(item)
            combiStr2.splice(index, 1)
            return true
        }
        newCombiStr1.push(item)
        return false
    })
    const union = [...intersection, ...newCombiStr1, ...combiStr2]


"""
