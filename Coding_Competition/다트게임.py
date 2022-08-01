"""
https://school.programmers.co.kr/learn/courses/30/lessons/17682
"""


def parsing(dartResult):
    idx_l = []
    d = dartResult
    for idx, val in enumerate(d):
        try:
            int(val)
            idx_l.append(idx)
        except:
            continue

    for i in idx_l:
        if i + 1 in idx_l:
            idx_l.remove(i + 1)

    game_list = []
    game_list.append(d[idx_l[0] : idx_l[1]])
    game_list.append(d[idx_l[1] : idx_l[2]])
    game_list.append(d[idx_l[-1] :])

    return game_list


def solution(dartResult):

    game_list = parsing(dartResult)

    # first
    result_list = []
    for idx, game in enumerate(game_list):
        result = 0
        try:
            n1 = int(game[:2])
            b1 = str(game[2])
            if len(game) == 4:
                o1 = str(game[3])
            else:
                o1 = 0
        except:
            n1 = int(game[0])
            b1 = str(game[1])
            if len(game) == 3:
                o1 = str(game[2])
            else:
                o1 = 0

        if b1 == "S":
            result += n1
        elif b1 == "D":
            result += n1 * n1
        elif b1 == "T":
            result += n1 * n1 * n1

        try:
            if o1 == "*":
                result = result * 2
                if idx >= 1:
                    result_list[idx - 1] = result_list[idx - 1] * 2
            elif o1 == "#":
                result = result * (-1)
        except:
            pass

        result_list.append(result)
        print(game)
        print(result_list)

    answer = 0
    for i in result_list:
        answer += i

    # print(result_list)
    return answer


def solution(dartResult):
    d = dartResult
    point = []
    answer = []
    d = d.replace("10", "k")
    point = ["10" if i == "k" else i for i in d]
    print(point)

    idx = -1
    sdt = ["S", "D", "T"]
    for j in point:
        if j.isdigit():
            answer.append(int(j))
            idx += 1
        elif j in sdt:
            answer[idx] = answer[idx] ** (sdt.index(j) + 1)
        elif j == "*":
            answer[idx] = answer[idx] * 2
            if idx >= 1:
                answer[idx - 1] = answer[idx - 1] * 2
        elif j == "#":
            answer[idx] = answer[idx] * (-1)

    return sum(answer)
