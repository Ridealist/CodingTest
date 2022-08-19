"""
https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
"""


def solution(survey, choices):

    type = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]

    char_dict = {}
    for i in type:
        char_dict[i] = {i[0]: 0, i[1]: 0}

    score_dict = {
        1: [3, 0],
        2: [2, 0],
        3: [1, 0],
        4: [0, 0],
        5: [0, 1],
        6: [0, 2],
        7: [0, 3],
    }

    for idx, s in enumerate(survey):
        score_dict[choices[idx]]
        char_dict[s][s[0]] += score_dict[choices[idx]][0]
        char_dict[s][s[1]] += score_dict[choices[idx]][1]

    result_dict = {"R": 0, "T": 0, "F": 0, "C": 0, "M": 0, "J": 0, "A": 0, "N": 0}

    for val in char_dict.values():
        for i in val.keys():
            result_dict[i] += val[i]

    # print(result_dict)

    answer = ""
    if result_dict["R"] >= result_dict["T"]:
        answer += "R"
    else:
        answer += "T"
    if result_dict["C"] >= result_dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if result_dict["J"] >= result_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if result_dict["A"] >= result_dict["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer


from functools import reduce


def solution(survey, choices):
    type = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    t = reduce(lambda x, y: x + y, type, "")
    char_dict = {}
    for i in set(list(t)):
        char_dict[i] = 0

    # score_dict = {
    #     1: [3, 0],
    #     2: [2, 0],
    #     3: [1, 0],
    #     4: [0, 0],
    #     5: [0, 1],
    #     6: [0, 2],
    #     7: [0, 3],
    # }

    for s, c in zip(survey, choices):
        if c <= 4:
            char_dict[s[0]] += 4 - c
        else:
            char_dict[s[1]] += c - 4

        # char_dict[s[0]] += score_dict[c][0]
        # char_dict[s[1]] += score_dict[c][1]

    # print(char_dict)

    types = ["RT", "CF", "JM", "AN"]

    answer = ""
    for type in types:
        if char_dict[type[0]] >= char_dict[type[1]]:
            answer += type[0]
        else:
            answer += type[1]

    return answer
